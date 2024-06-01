"""merge rule-set for karing


- outbound:
    - direct_out    直连
    - block_out     屏蔽
    - selector_out  自动选择[default]
    - selected_out  当前选择

 - default
    - geoip/[area].srs
    - geosite/[area].srs

cn:
    - https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash/config
        - ACL4SSR_Online_Full.ini
        - ACL4SSR_Online.ini

"""

OPT_RULESET_GROUPS = {}
OPT_RULESET_GROUPS['default'] = {
    '🛑 Adblock': {
        'default': 'on',
        'outbound': 'block_out',
        'rules': [
            'acl:BanAD',
            'geosite:ads',
        ],
    },
    'Ⓜ️ Bing': {
        'default': 'off',
        'outbound': 'selector_out',
        'rules': ['geoip:bing', 'geosite:bing'],
    },
    'Ⓜ️ OneDrive': 'geosite:onedrive',
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
    '🛑 广告拦截': {
        'default': 'on',
        'outbound': 'block_out',
        'rules': [
            'acl:BanAD',
            'geosite:ads',
        ],
    },
    '🍃 应用净化': 'acl:BanProgramAD',
    '📢 谷歌FCM': {'outbound': 'selector_out', 'rules': 'Ruleset/GoogleFCM'},
    'Ⓜ️ 微软Bing': 'Bing',
    'Ⓜ️ 微软云盘': 'OneDrive',
    'Ⓜ️ 微软服务': 'Microsoft',
    '🍎 苹果服务': 'Apple',
    '📲 电报消息': 'Telegram',
    '💬 OpenAi': 'Ruleset/OpenAi',
    '🎶 网易音乐': 'Ruleset/NetEaseMusic',
    '🎮 游戏平台': [
        'acl:Epic',
        'Ruleset/Origin',
        'Ruleset/Sony',
        'Ruleset/Steam',
        'Ruleset/Nintendo',
    ],
    '📹 油管视频': 'Ruleset/YouTube',
    '🎥 奈飞视频': 'Ruleset/Netflix',
    '📺 巴哈姆特': 'Ruleset/Bahamut',
    '📺 哔哩哔哩': [
        'Ruleset/BilibiliHMT',
        'Ruleset/Bilibili',
    ],
    '🌏 国内媒体': 'ChinaMedia',
    '🌍 国外媒体': 'ProxyMedia',
    '🚀 国外服务': 'ProxyGFWlist',
}
##end china

##start iran
OPT_RULESET_GROUPS['ir'] = OPT_RULESET_GROUPS['default'].copy()
OPT_RULESET_GROUPS['ir']['🛑 Adblock'] = {
    'default': 'on',
    'outbound': 'block_out',
    'rules': ['acl:BanAD', 'geosite:ads', 'geosite:category-ads-ir'],
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

# "rules": [
#   {
#   {
#     "rule_set": [
#       "geosite:6park"
#     ],
#     "outbound": "🇰🇷【TUIC】韩国 BGP D06",
#     "name": "6park[geosite]"
#   },
#   {
#     "rule_set": [
#       "geoip:bing"
#     ],
#     "outbound": "selector_out",
#     "name": "bing[geoip]"
#   },
#   {
#     "rule_set": [
#       "acl:BanAD"
#     ],
#     "outbound": "block_out",
#     "name": "BanAD[acl]"
#   },
#   {
#     "rule_set": [
#       "acl:Amazon"
#     ],
#     "outbound": "selector_out",
#     "name": "Amazon[acl]"
#   },
#   {
#     "rule_set": [
#       "acl:BBC"
#     ],
#     "outbound": "🇰🇷【TUIC】韩国 BGP D06",
#     "name": "BBC[acl]"
#   },
#   {
#     "rule_set": [
#       "geosite:cn"
#     ],
#     "outbound": "direct_out",
#     "name": "cn[geosite]"
#   },
#   {
#     "rule_set": [
#       "geoip:cn"
#     ],
#     "outbound": "direct_out",
#     "name": "cn[geoip]"
#   }
# ],
# "rule_set": [
#       {
#         "tag": "acl:BanAD",
#         "type": "local",
#         "format": "binary",
#         "path": "D:\\Program Files\\Karing\\data\\flutter_assets\\assets\\datas\\acl\\BanAD.srs"
#       },


def maker_for_area(area: str, config: dict):
    pass


if __name__ == '__main__':
    for area, config in OPT_RULESET_GROUPS.items():
        maker_for_area(area, config)
