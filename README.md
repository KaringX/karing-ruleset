# rule-set collection for sing-box/karing

## Thanks to
- [meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat/raw/sing/geo)
- [Chocolate4U-Iran](https://github.com/Chocolate4U/Iran-sing-box-rules/tree/rule-set?tab=readme-ov-file)
- [ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)


# sing-box/karing rule-set规则碎片
- 基于ACL4SSR和geoip、geosite规则源文件生成的json和srs规则文件
    - 推荐配合[karing](https://github.com/KaringX/karing)食用更佳

## 下载链接
### 方案1 github
- 比如需要国内IP直连, 对应文件为 `ChinaIp.srs`
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




