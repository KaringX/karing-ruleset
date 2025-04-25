# rule-set collection for sing-box/karing

## Contents
- [GeoIp/GeoSite](https://github.com/KaringX/karing-ruleset/tree/workflow?tab=readme-ov-file#geoipgeosite)
- [ACL4SSR](https://github.com/KaringX/karing-ruleset/tree/workflow?tab=readme-ov-file#sing-boxkaring-rule-set%E8%A7%84%E5%88%99%E7%A2%8E%E7%89%87)
- [AdGuardSDNSFilter](https://github.com/KaringX/karing-ruleset/tree/workflow?tab=readme-ov-file#adguardsdnsfilter)


## Thanks to
- [meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat/raw/sing/geo)
- [Chocolate4U/Iran-v2ray-rules](https://github.com/Chocolate4U/Iran-v2ray-rules)
- [ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)
- Thank you for suggesting modifications to the recommendation rules and for adding the routing rules of Iran:
    - [@AmirhosseinBrooklyn](https://github.com/AmirhosseinBrooklyn) (BrooklynVPN & Daricheh)
    - [@Phoenix-999](https://github.com/Phoenix-999)
- [savely-krasovsky/antizapret-sing-box](https://github.com/savely-krasovsky/antizapret-sing-box/)
    - Lists of domain and IPs blocked in Russia in Rule Set form
- [runetfreedom/russia-v2ray-rules-dat](https://github.com/runetfreedom/russia-v2ray-rules-dat)
    - Этот репозиторий содержит автоматически обновляемые правила маршрутизации V2Ray, основанные на данных о заблокированных доменах и адресах в России.

## Welcome to submit your preferred rule-set
- [submit your preferred rule-set](https://github.com/KaringX/karing-ruleset/issues/2)
- [欢迎提交你中意的规则集](https://github.com/KaringX/karing-ruleset/issues/1)

## Description
- karing 1.0.23.263 and later versions will default to including all rules from this repository.
- Please use the latest version of sing-box, as versions before 1.9 had issues with domain name matching. For example, 'google.com' was incorrectly matching 'le.com'."
    - [Improve domain suffix match behavior](https://github.com/SagerNet/sing/commit/4d96f15eca075f4b5535053304d54812fdfa96e0)

# GeoIP/GeoSite
## 🇷🇺 Russia
- howto use [runetfreedom/russia-v2ray-rules-dat](https://github.com/runetfreedom/russia-v2ray-rules-dat) or  [savely-krasovsky/antizapret-sing-box](https://github.com/savely-krasovsky/antizapret-sing-box/) in karing
    - be like: `antizapret.srs`
    - Add New Diversion Group
        - -> fill in srs url
        - `https://github.com/savely-krasovsky/antizapret-sing-box/releases/latest/download/antizapret.srs`
        - -> save rule-set
    - return to Diversion Rules Page, Custom Diversion Group
        - -> select the newly created Diversion Group
        - -> Action selection is `Current Select`
    - **Note** Please pay attention to the size of the SRS file, such as being greater than **3M**, it should only be used on **Windows**, there is a possibility of exceeding the memory limit on Android and iOS.

- The source files about Russia are from **russia-v2ray-rules-dat**
    ```
    geoip/
        blocked@ru.srs
        blocked-community@ru.srs
        re-filter@ru.srs

    geosite
        blocked@ru.srs
        available-only-inside@ru.srs

    ```



## <img src="https://flagofiran.com/files/flag-of-iran-emoji-ios.png" alt="Iran emoji" style="width:1em; height:1em; vertical-align:text-bottom;"> Iran
- The source files about Iran come from **Chocolate4U**
    ```
    geoip/
        amazon.srs
        arvancloud.srs
        bing.srs
        derakcloud.srs
        digitalocean.srs
        github.srs
        iranserver.srs
        ir.srs
        linode.srs
        malware.srs
        microsoft.srs
        openai.srs
        oracle.srs
        parspack.srs
        phishing.srs

    geosite
        ads.srs
        category-ads-ir.srs
        category-bank-ir.srs
        category-bourse-ir.srs
        category-education-ir.srs
        category-forums-ir.srs
        category-gov-ir.srs
        category-insurance-ir.srs
        category-ir.srs
        category-media-ir.srs
        category-news-ir.srs
        category-payment-ir.srs
        category-scholar-ir.srs
        category-shopping-ir.srs
        category-social-media-ir.srs
        category-tech-ir.srs
        category-travel-ir.srs
        cn@ads.srs
        cryptominers.srs
        geolocation-!cn@ads.srs
        geolocation-cn@ads.srs
        ir.srs
        malware.srs
        nsfw.srs
        phishing.srs
        social.srs

    ```

## description
- geosite的一些说明:
    ```
    geosite:category-ads　包含了常见的广告域名。
    geosite:category-ads-all　包含了常见的广告域名，以及广告提供商的域名。
    geosite:cn　相当于 geolocation-cn 和 tld-cn 的合集。
    geosite:apple　包含了 Apple 旗下绝大部分域名。
    geosite:google　包含了 Google 旗下绝大部分域名。
    geosite:microsoft　包含了 Microsoft 旗下绝大部分域名。
    geosite:facebook　包含了 Facebook 旗下绝大部分域名。
    geosite:twitter　包含了 Twitter 旗下绝大部分域名。
    geosite:telegram　包含了 Telegram 旗下绝大部分域名。
    geosite:geolocation-cn　包含了常见的大陆站点域名。
    geosite:geolocation-!cn　包含了常见的非大陆站点域名，同时包含了 tld-!cn。
    geosite:tld-cn　包含了 CNNIC 管理的用于中国大陆的顶级域名，如以 .cn、.中国 结尾的域名。
    geosite:tld-!cn　包含了非中国大陆使用的顶级域名，如以 .hk（香港）、.tw（台湾）、.jp（日本）、.sg（新加坡）、.us（美国）.ca（加拿大）等结尾的域名。
    ```

# sing-box/karing rule-set规则碎片
- 基于ACL4SSR和geoip、geosite规则源文件生成的json和srs规则文件
    - 推荐配合[karing](https://github.com/KaringX/karing)食用更佳

## 下载链接
### 方案1 github
### Chocolate4U GeoIP/GeoSite (Iran)
- **GeoIP**: `geoip.dat` from [Chocolate4U Latest Release](https://raw.githubusercontent.com/Chocolate4U/Iran-v2ray-rules/latest-release/geoip.dat)
- **GeoSite**: `geosite.dat` from [Chocolate4U Latest Release](https://raw.githubusercontent.com/Chocolate4U/Iran-v2ray-rules/latest-release/geosite.dat)

### ChinaIp.srs
- 访问链接:
https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/ChinaIp.srs

### 方案2 CDN:jsdelivr
- 比如需要去广告功能, 对应文件为 `BanAD.srs`
- 访问链接:
https://fastly.jsdelivr.net/gh/karingX/karing-ruleset@sing/ACL4SSR/BanAD.srs

## 规则碎片

- 主要文件在**sing分支**根目录和*ACL4SSR/Ruleset*文件夹下，可以配合一些订阅转换或者代理工具进行使用。

- 下面是部分文件的注释，所有文件列表查看 [sing分支目录](https://github.com/KaringX/karing-ruleset/tree/sing)

| 文件                   | 类型                 | 解释                                                         |
| ---------------------- | -------------------- | ------------------------------------------------------------ |
| BanAD.srs             | 规则碎片-去广告      | 只包含常见广告关键字、广告联盟。无副作用，放心使用           |
| BanADCompany.srs             | 规则碎片-去广告      | 包含各大公司的广告域名, 数据来源:[adblock_data.json](https://github.com/d3ward/toolz/raw/master/src/data/adblock_data.json)           |
| BanProgramAD.srs      | 规则碎片-去广告      | 包含常用应用的各种去广告规则。可能有轻微副作用，可放心使用。（如果网站功能和广告冲突，会删掉去广告规则） |
| BanEasyListChina.srs  | 规则碎片-去广告      | AdblockPlus中的中国所有的屏蔽域名                            |
| LocalAreaNetwork.srs  | 规则碎片-直连        | 本地地址和路由器直连域名啥的                                 |
| ChinaDomain.srs       | 规则碎片-直连        | 国内常见域名、直连CDN等。（很全，常用网址都有）              |
| ChinaCompanyIp.srs    | 规则碎片-直连        | 国内BAT公司及云服务厂商的IP段。所有在该云服务上的网站都可以直连。比如你网站在阿里云香港都可以直连。 |
| ChinaIp.srs           | 规则碎片-直连        | IPIP的国内地址段。比GeoIp更好。电脑性能好，可以引入          |
| Download.srs          | 规则碎片-直连        | 一些下载用的域名                                             |
| Apple.srs             | 规则碎片             | 苹果公司的所有域名                                           |
| Microsoft.srs         | 规则碎片             | 微软公司的所有域名                                           |
| OneDrive.srs          | 规则碎片             | OneDrive                                                     |
| GoogleCN.srs          | 规则碎片-直连        | 谷歌在中国能直连的网址列表                                   |
| Telegram.srs          | 规则碎片-代理        | Telegram的所有域名                                           |
| Netflix.srs           | 规则碎片-代理        | Netflix的所有域名                                            |
| ProxyGFWlist.srs      | 规则碎片-代理        | GFW的全量列表                                                |
| ProxyLite.srs         | 规则碎片-代理        | 比较精简的代理列表，包含常用的，以及被污染的域名             |


# AdGuardSDNSFilter
- AdGuardFilter
    - source: https://raw.githubusercontent.com/AdguardTeam/AdGuardSDNSFilter/master/configuration.json
    - srs list: [AdGuardFilter.list](https://github.com/KaringX/karing-ruleset/tree/sing/AdGuard/AdGuardFilter.list)
- PopupFilter
    - source: https://raw.githubusercontent.com/AdguardTeam/AdGuardSDNSFilter/master/configuration_popup_filter.json
    - srs list: [PopupFilter.list](https://github.com/KaringX/karing-ruleset/tree/sing/AdGuard/PopupFilter.list)
- ppfeuferFilter
    - source: https://raw.githubusercontent.com/ppfeufer/adguard-filter-list/master/hostlist-compiler-config.json
    - srs list: [ppfeuferFilter.list](https://github.com/KaringX/karing-ruleset/tree/sing/AdGuard/ppfeuferFilter.list)
