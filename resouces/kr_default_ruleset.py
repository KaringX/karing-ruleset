"""merge rule-set for karing


- outbound:
    - direct_out    直连
    - block_out     屏蔽
    - selector_out  当前选择[default]

 - default
    - geoip/[area].srs
    - geosite/[area].srs

- cn:
    - https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash/config
        - ACL4SSR_Online_Full.ini
        - ACL4SSR_Online.ini
- Adblock
    - category-ads 包含了常见的广告域名
    - category-ads-all 包含了常见的广告域名，以及广告提供商的域名

"""

import sys
import os
import json


def debug_log(msg: str):
    print(msg)
    pass


OPT_RULESET_GROUPS = {}
OPT_RULESET_GROUPS['default'] = {
    '🛑 Adblock': {
        'default': 'on',
        'outbound': 'block_out',
        'rules': [
            'acl:BanAD',
            'geosite:category-ads',
        ],
    },
    'Ⓜ️ Bing': {
        'default': 'off',
        'outbound': 'selector_out',
        'rules': ['geoip:bing', 'geosite:bing'],
    },
    'Ⓜ️ OneDrive': {
        'default': 'off',
        'outbound': 'direct_out',
        'rules': [
            'geosite:onedrive',
        ],
    },
    'Ⓜ️ Microsoft': {
        'default': 'off',
        'outbound': 'selector_out',
        'rules': [
            'geosite:microsoft',
            'geosite:microsoft-dev',
            'geosite:microsoft-pki',
        ],
    },
    '🍎 Apple': {
        'default': 'off',
        'outbound': 'direct_out',
        'rules': [
            'geosite:apple',
            'geosite:apple-ads',
            'geosite:apple-dev',
            'geosite:apple-pki',
            'geosite:apple-update',
        ],
    },
    '📲 Telegram': ['geoip:telegram', 'geosite:telegram'],
    '💬 OpenAi': ['geoip:openai', 'geosite:openai'],
    '🎮 Game': [
        'acl:Epic',
        'acl:Origin',
        'acl:Sony',
        'acl:Steam',
        'acl:Nintendo',
    ],
    '📹 YouTube': ['geosite:youtube'],
    '🎥 Netflix': ['geoip:netflix', 'geosite:netflix'],
}

## start china
OPT_RULESET_GROUPS['cn'] = {
    '🛑 广告拦截': {
        'default': 'on',
        'outbound': 'block_out',
        'rules': [
            'acl:BanAD',
            'geosite:category-ads',
        ],
    },
    '🍃 应用净化': {
        'default': 'on',
        'outbound': 'block_out',
        'rules': ['acl:BanProgramAD'],
    },
    '🎯 国内直连': {
        'default': 'on',
        'outbound': 'direct_out',
        'rules': [
            'acl:LocalAreaNetwork',
            'acl:UnBan',
            'acl:GoogleCN',
            'acl:SteamCN',
            'acl:ChinaIp',
            'acl:ChinaDomain',
            'acl:ChinaCompanyIp',
            'acl:Download',
        ],
    },
    '🌏 国内媒体': {
        'default': 'on',
        'outbound': 'direct_out',
        'rules': ['acl:ChinaMedia'],
    },
    '🚀 国外媒体': {
        'default': 'on',
        'outbound': 'selector_out',
        'rules': [
            'acl:ProxyMedia',
            'acl:ProxyGFWlist',
        ],
    },
    'Ⓜ️ 微软Bing': {
        'default': 'off',
        'outbound': 'selector_out',
        'rules': ['geoip:bing', 'geosite:bing'],
    },
    'Ⓜ️ 微软云盘': {
        'default': 'off',
        'outbound': 'direct_out',
        'rules': [
            'geosite:onedrive',
        ],
    },
    'Ⓜ️ 微软服务': {
        'default': 'off',
        'outbound': 'selector_out',
        'rules': [
            'geosite:microsoft',
            'geosite:microsoft-dev',
            'geosite:microsoft-pki',
        ],
    },
    '🍎 苹果服务': {
        'default': 'off',
        'outbound': 'direct_out',
        'rules': [
            'geosite:apple',
            'geosite:apple-ads',
            'geosite:apple-dev',
            'geosite:apple-pki',
            'geosite:apple-update',
        ],
    },
    '📲 电报消息': ['geoip:telegram', 'geosite:telegram'],
    '💬 OpenAi': ['geoip:openai', 'geosite:openai'],
    '🎶 网易音乐': {
        'default': 'off',
        'outbound': 'direct_out',
        'rules': [
            'acl:NetEaseMusic',
        ],
    },
    '🎮 游戏平台': [
        'acl:Epic',
        'acl:Origin',
        'acl:Sony',
        'acl:Steam',
        'acl:Nintendo',
    ],
    '📹 油管视频': ['geosite:youtube'],
    '🎥 奈飞视频': ['geoip:netflix', 'geosite:netflix'],
    '📺 巴哈姆特': 'acl:Bahamut',
    '📺 哔哩哔哩': {
        'default': 'on',
        'outbound': 'direct_out',
        'rules': [
            'acl:BilibiliHMT',
            'acl:Bilibili',
        ],
    },
    '📢 谷歌FCM': {
        'default': 'off',
        'outbound': 'direct_out',
        'rules': [
            'acl:GoogleFCM',
        ],
    },
}
##end china

##start iran
OPT_RULESET_GROUPS['ir'] = OPT_RULESET_GROUPS['default'].copy()
OPT_RULESET_GROUPS['ir']['🛑 Adblock'] = {
    'default': 'on',
    'outbound': 'block_out',
    'rules': [
        'geosite:category-ads',
        'geosite:category-ads-ir',
    ],
}
OPT_RULESET_GROUPS['ir']['🛑 malware'] = {
    'default': 'off',
    'outbound': 'block_out',
    'rules': ['geosite:malware'],
}
OPT_RULESET_GROUPS['ir']['📢 phishing'] = {
    'default': 'off',
    'outbound': 'direct_out',
    'rules': ['geoip:phishing', 'geosite:phishing'],
}
OPT_RULESET_GROUPS['ir']['☁️ parspack'] = {
    'default': 'off',
    'outbound': 'direct_out',
    'rules': ['geoip:parspack'],
}
##end iran


def maker_for_area(area: str, config: dict, root_path: str) -> bool:
    # config dir/file
    cfg_dir = os.path.join(root_path, 'karing')
    if not os.path.exists(cfg_dir):
        os.mkdir(cfg_dir)
        debug_log(f"mkdir {cfg_dir}")

    cfg_file = os.path.join(cfg_dir, f"{area}.json")

    # for each group
    route_dict = {'rules': {}, 'rule_set': {}}
    for gkey, gval in config.items():
        msg = f"area:{area} gkey:{gkey}"
        gval = maker_one_row(gval)

        for rule_set in gval['rules']:
            if not rule_file_exists(rule_set, root_path=root_path):
                debug_log(f"ERR: {msg} {rule_set} srs file not exists")
                return
            # rule set
            route_dict['rule_set'][rule_set] = maker_one_rule_set(rule_set)
            # END for rule set

        # rules
        rule = maker_one_rule(name=gkey, group=gval)
        route_dict['rules'][rule['name']] = rule

        # END for

    # convert to list
    route_dict['rule_set'] = list(route_dict['rule_set'].values())
    route_dict['rules'] = list(route_dict['rules'].values())

    json_string = json.dumps({'route': route_dict})
    with open(cfg_file, "w") as json_file:
        json_file.write(json_string)
        debug_log(f"wirte to {cfg_file}")
        return True

    return False


def maker_one_rule(name: str, group: dict) -> dict:
    outbound = group['outbound']
    rule_set = group['rules']
    return {
        "rule_set": rule_set,
        "outbound": outbound,
        "name": f"{name}[karing]",
        'switch': group['default'],
    }


def maker_one_rule_set(rule: str) -> dict:
    splits = rule.split(':')
    row = {
        "tag": "acl:BanAD",
        "type": "local",
        "format": "binary",
        "path": "acl/BanAD.srs",
    }
    row['tag'] = rule
    row['path'] = f"{splits[0]}/{splits[1]}.srs"
    return row


def maker_one_row(gval: any) -> dict:
    OPT_DEFAULT_GRULE = {'default': 'off', 'outbound': 'selector_out', 'rules': []}

    vtype = type(gval)
    if vtype is str:
        tmp_val = gval
        gval = OPT_DEFAULT_GRULE
        gval['rules'] = [tmp_val]
    elif vtype is list:
        tmp_val = gval
        gval = OPT_DEFAULT_GRULE
        gval['rules'] = tmp_val
    elif vtype is dict:
        if 'rules' not in gval:
            raise ValueError(f"ERR: rules not in gval:{gval}")

        row = OPT_DEFAULT_GRULE
        row.update(gval)
        gval = row

    else:
        raise ValueError(f"ERR: type:{vtype} gval:{gval}")

    return gval


def rule_file_exists(rule: str, root_path: str) -> bool:
    splits = rule.split(':')
    if splits[0] == 'acl':
        rule_dir = os.path.join(root_path, 'ACL4SSR')
    elif splits[0] == 'geoip':
        rule_dir = os.path.join(root_path, 'geo/geoip')
    elif splits[0] == 'geosite':
        rule_dir = os.path.join(root_path, 'geo/geosite')
    else:
        raise ValueError(f"unkown rule dir:{splits}")

    rule_file = os.path.join(rule_dir, f"{splits[1]}.srs")
    return os.path.exists(rule_file)


def main():
    if len(sys.argv) < 2:
        deug_log("Usage: python script.py <srs_file_root_path>")
        return

    root_path = sys.argv[1]
    if not os.path.isdir(root_path):
        deug_log(f"path:{root_path} not dir")
        return

    root_path = os.path.abspath(root_path)
    for area, config in OPT_RULESET_GROUPS.items():
        maker_for_area(area, config, root_path)


if __name__ == '__main__':
    main()
