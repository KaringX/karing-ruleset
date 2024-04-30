# list convert to json
import sys
import os
import json

MAP_RULES_KEY_DICT = {
    'IP-CIDR': 'ip_cidr',
    'IP-CIDR6': 'ip_cidr',
    'DOMAIN': 'domain',
    'DOMAIN-SUFFIX': 'domain_suffix',
    'DOMAIN-KEYWORD': 'domain_keyword',
    'PROCESS-NAME': 'process_name',
}


def deug_log(msg: str):
    print(msg)
    pass


def main(src_path: str, out_path: str = None):
    out_path = (
        os.getcwd()
        if out_path is None or len(out_path) == 0
        else os.path.abspath(out_path)
    )
    src_path = os.path.abspath(src_path)
    deug_log(f"{src_path} to {out_path}")
    listdir_format(src_path, out_path=out_path)


def listdir_format(src_path: str, out_path: str):
    for item in os.listdir(src_path):
        if os.path.isdir(item):
            out_path2 = os.path.join(out_path, item)
            if os.path.exists(out_path2) is False:
                os.mkdir(out_path2)
                deug_log(f"mkdir {out_path2}")
            listdir_format(os.path.join(src_path, item), out_path=out_path2)
        else:
            converto_json(os.path.join(src_path, item), out_path=out_path)


def converto_json(src_file: str, out_path: str):
    splits = os.path.splitext(src_file)
    if splits[1] != ".list":
        return
    if not os.path.isfile(src_file):
        deug_log(f"ERROR FILE: {src_file}")
        return

    out_file = os.path.join(out_path, os.path.basename(splits[0]) + ".json")
    content = {"version": 1, "rules": [{}]}

    with open(src_file, "r") as f:
        line = f.readline()
        while line:
            # line.strip()
            in_key = False
            row = line.split(",")
            if len(row) >= 2:
                rule, cont = row[0].upper(), row[1].strip()
                if rule in MAP_RULES_KEY_DICT:
                    rkey = MAP_RULES_KEY_DICT[rule]
                    if rkey in content['rules'][0]:
                        content['rules'][0][rkey].append(cont)
                    else:
                        content['rules'][0][rkey] = [cont]

                    in_key = True
                # END if

            #! DEBUG
            if in_key is False:
                if row[0] not in ["USER-AGENT", "URL-REGEX"] and line[0] not in [
                    '#',
                    '\n',
                ]:
                    deug_log(f"row:{row} first:{line[0]} UNKOWN")
            line = f.readline()
            # END while

    if len(content['rules'][0]) == 0:
        return

    json_string = json.dumps(content)
    with open(out_file, "w") as json_file:
        json_file.write(json_string)
        deug_log(f"wirte to {out_file}")
    # END converto_josn


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <first_parameter> <second_parameter>")
    else:
        src_path = sys.argv[1]
        out_path = sys.argv[2]
        main(src_path, out_path)
