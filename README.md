# 酒井科协秋培 2026

2026 秋季学期基础技能培训主页。严格沿用 [sast-summer-training-2026](https://github.com/sast-summer-training-2026/sast-summer-training-2026.github.io) 的 MkDocs Material 配置、样式和页面结构，仅替换培训名称、预告链接和已提供的课程材料。暑培课程与录像不作为本期内容。

## 构建

```sh
pip install -r requirements.txt
mkdocs build --strict
```

生成目录为 `site/`。

## 内容

- 首页：`docs/index.md`
- 课程索引：`docs/basic/index_basic.md`
- Coding Agent：`docs/basic/coding-agent/index.md`
- 附件原件：`docs/basic/coding-agent/coding-agent-lecture.html`

预告：https://mp.weixin.qq.com/s/SepHT5yKPReIadTMS84KnQ 。课程信息依据用户提供的预告正文录入；报名二维码请在原推送中查看。

## 发布

当前 GitHub Pages 使用 `main` 分支的根目录。源码保留在 `docs/`，构建产物同时保存于仓库根目录；`.nojekyll` 让 Pages 直接提供静态页面。`.github/workflows/pages.yml` 验证 MkDocs 构建，GitHub 自带的 `pages-build-deployment` 工作流负责发布。

修改源码后，在安装了依赖的 Python 环境中运行：

```sh
python scripts/build_site.py
git add .
git commit -m "Update training website"
git push origin HEAD:main
```

脚本严格构建并根据 `.site-files.json` 更新发布文件，不覆盖源码或未知文件。确认 GitHub Pages 设置为 **Deploy from a branch → main → / (root)**。发布后查看 `pages-build-deployment` 的结果。
