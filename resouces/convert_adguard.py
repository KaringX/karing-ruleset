# AdGuardSDNSFilter list convert to srs
# from
#   https://github.com/AdguardTeam/AdGuardSDNSFilter
#   https://github.com/ppfeufer/adguard-filter-list
# Use
#   sing-box rule-set convert --type adguard [--output <file-name>.srs] <file-name>.txt to convert to binary rule-set.

import sys
import os
import json
import subprocess

from helper.helper import (
    debug_log,
    get_out_path,
    get_url_content,
    writeto_rulefile,
    correct_name,
    remove_ansi_escape_codes,
)

# TODO exclusions.txt
# https://raw.githubusercontent.com/AdguardTeam/AdGuardSDNSFilter/master/Filters/exclusions.txt


SING_BOX_EXEC_PATH = None

ADGUARD_CONFIG_FILTER_LIST = [
    # {
    #     'name': 'AdGuardFilter',
    #     'source': 'https://raw.githubusercontent.com/AdguardTeam/AdGuardSDNSFilter/master/configuration.json',
    # },
    # {
    #     'name': 'PopupFilter',
    #     'source': 'https://raw.githubusercontent.com/AdguardTeam/AdGuardSDNSFilter/master/configuration_popup_filter.json',
    # },
    # {
    #     'name': 'ppfeuferFilter',
    #     'source': 'https://raw.githubusercontent.com/ppfeufer/adguard-filter-list/master/hostlist-compiler-config.json',
    # },
    {
        'name': 'HostlistsRegistry',
        'source': 'https://adguardteam.github.io/HostlistsRegistry/assets/filters.json',
    },
]

SOURCE_REPLACE_DICT = {
    # # Get OISD list, since the HostlistCompiler can't fetch it for whatever reason » https://github.com/AdguardTeam/HostlistCompiler/issues/58
    "../oisd.txt": "https://big.oisd.nl/",
}


def converto_srs(out_path: str, file_name: str) -> bool:
    sb_exe_path = SING_BOX_EXEC_PATH
    out_file = os.path.join(out_path, file_name + '.srs')
    src_file = os.path.join(out_path, file_name + '.txt')

    # debug_log(f"convering ... {out_file}")
    command = (
        f"{sb_exe_path} rule-set convert --type adguard --output {out_file} {src_file}"
    )
    # debug_log(command)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # if result.stderr:
    # Filter out lines that start with "DEBUG"
    error_lines = [
        line for line in result.stderr.splitlines() if not line.startswith("DEBUG")
    ]
    error_msg = error_lines[-1] if len(error_lines) > 0 else ""

    debug_log(
        f"Convert code:{result.returncode} error:{error_msg} output:{result.stdout}"
    )
    if result.returncode == 0:
        debug_log(f"Convert {os.path.basename(out_file)} success")
        return True

    return True if remove_ansi_escape_codes(error_msg).startswith('INFO') else False
    # END converto_srs


def main(out_path: str = None):
    # check out dir
    if not os.path.isdir(out_path):
        debug_log(f"ERR: {out_path} not exist")
        exit(1)

    # mkdir
    out_path = os.path.abspath(out_path)
    out_path2 = os.path.join(out_path, 'AdGuard')
    if not os.path.exists(out_path2):
        os.mkdir(out_path2)
        debug_log(f"mkdir {out_path2}")

    # check sing-box
    sb_exe_path = os.path.join(out_path, 'sing-box')
    if not os.path.isfile(sb_exe_path):
        debug_log(f"ERR: {sb_exe_path} not exist")
        exit(1)
    global SING_BOX_EXEC_PATH
    SING_BOX_EXEC_PATH = sb_exe_path

    for item in ADGUARD_CONFIG_FILTER_LIST:
        compile_filterlist(out_path=out_path2, item=item)

    # END main


def compile_filterlist(out_path: str, item: dict):
    source = item['source']

    name = correct_name(item['name'])
    out_path2 = os.path.join(out_path, name)
    if not os.path.exists(out_path2):
        os.mkdir(out_path2)
    if not os.path.isdir(out_path2):
        debug_log(f"ERR: {out_path2} mkdir fail!")
        exit(1)

    debug_log(f"\n\n\t\x1b[36mCompiling\x1b[0m [[{name}]] => {source}")
    content = get_url_content(source)
    if content is None:
        return False

    # sucess list
    succ_path = os.path.join(out_path, f"{name}.list")
    succ_list = []
    fitems = {}

    try:
        # 如果json_data已经是字典，直接使用
        if isinstance(content, str):
            data = json.loads(content)
        else:
            data = content

        # 判断并赋值
        if 'sources' in data:
            fitems = data['sources']
            debug_log(f"{name} 找到 sources 已赋值给 fitems")
        elif 'filters' in data:
            fitems = data['filters']
            debug_log(f"{name} 找到 filters 已赋值给 fitems")
        else:
            raise ValueError(f"{name} JSON数据中既不包含'sources'也不包含'filters'字段")

    except json.JSONDecodeError as e:
        debug_log(f"JSON解码错误: {e}")
        return None
    except ValueError as e:
        debug_log(f"错误: {e}")
        return None

    # 解析每一项
    for filter_item in fitems:
        ret = compile_filterone(out_path2, filter_item)
        if ret is True:
            if 'filterKey' in filter_item:
                fname = filter_item['filterKey']
            else:
                fname = filter_item['name']
            succ_list.append(correct_name(fname) + '.srs')

    # wirte sucess list
    writeto_rulefile(succ_path, "\n".join(succ_list))

    # END compile


def compile_filterone(out_path: str, item: dict) -> bool:
    if 'downloadUrl' in item:
        source = item['downloadUrl']
    else:
        source = item['source']
    if source in SOURCE_REPLACE_DICT:
        source = SOURCE_REPLACE_DICT[source]

    if 'filterKey' in item:
        fname = item['filterKey']
    else:
        fname = item['name']

    #!TEST
    # if fname != 'hagezi_ultimate':
    #     return False

    name = correct_name(fname)
    debug_log(f"\n\tdownloading [ {name} ] => {source}")
    content = get_url_content(source)
    if content is None:
        return False

    # write file
    out_file = os.path.join(out_path, name + '.txt')
    writeto_rulefile(out_file, content)

    # convert srs
    return converto_srs(out_path, name)
    # END compile one


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\x1b[31mUsage\x1b[0m: python script.py <output path>")
    else:
        out_path = get_out_path(sys.argv[1])
        main(out_path)

# END FILE
