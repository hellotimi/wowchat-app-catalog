# WowChat 应用目录

纯静态应用配置、图标和配方包，不需要 Node.js、数据库或 Ferdium API。

目录地址：https://hellotimi.github.io/wowchat-app-catalog/apps.json

已包含 Gmail、微信、WhatsApp、Telegram、Facebook、Discord。

## 自己维护应用

直接在 GitHub 编辑根目录 `apps.json` 并提交，GitHub Pages 会自动发布。

| 字段 | 用途 |
|---|---|
| enabled | false 隐藏应用并禁止新增安装，不删除已登录的应用 |
| featured | 是否推荐 |
| order | 显示顺序，越小越靠前 |
| name | 显示名称 |
| aliases | 搜索别名 |
| icon | 相对于 apps.json 的 SVG 路径 |
| package | 相对于 apps.json 的配方包路径 |
| version | 配方版本 |
| sha256 | 安装包 SHA-256，客户端安装前校验 |
| size | 压缩包字节数 |

客户端启动时读取远程配置，进程内缓存；更改后重启客户端。网络不可用时回退到已缓存目录或随程序内置的目录。

## 修改网址和配方

修改 `sources/应用ID/package.json` 的 `config.serviceURL`，或修改同目录内的网页脚本和样式。
修改版本后运行 `python tools/package.py`，它会重新打包、复制图标，并更新 apps.json 中的版本、SHA-256 和文件大小。
将源码、apps.json、icons 和 packages 的变化一起提交到 GitHub。已安装的配方不会被自动覆盖。

## 发布

GitHub 仓库 Settings → Pages → Deploy from a branch → main → /(root)。
根目录 `.nojekyll` 使目录按静态文件发布，无需构建。所有资源均为公开应用集成文件，不要上传账号、Token 或业务数据。

## 来源

配方源码取自 Ferdium 开源配方仓库，来源提交见 UPSTREAM.json，许可证见 UPSTREAM-LICENSE.md 及各配方自带 LICENSE。
运行时不需要连接 Ferdium。各应用本身仍需连接对应的 Google、微信、Meta、Telegram、Discord 网站。
