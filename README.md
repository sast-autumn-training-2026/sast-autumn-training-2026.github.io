# 酒井科协秋培 2026

2026 秋季学期基础技能培训主页，沿用暑培站点的 MkDocs Material 结构。

## 本地开发

需要 Python 3.10 或更新版本。

```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
mkdocs serve -a 0.0.0.0:8000
```

构建检查：`mkdocs build --strict`。生成目录为 `site/`。

## 更新内容

- 首页：`docs/index.md`
- 培训安排：`docs/schedule.md`
- Coding Agent：`docs/basic/coding-agent/index.md`
- 原始讲义：`docs/basic/coding-agent/coding-agent-lecture.html`（保持附件原样）

培训预告：[微信公众号](https://mp.weixin.qq.com/s/SepHT5yKPReIadTMS84KnQ)。当前云实例访问预告仍被网络策略拦截，完整课程、时间地点和报名信息待核实后补充；未将暑期课程误作为秋季安排。Logo 与 favicon 沿用暑期培训仓库的 SAST 资产。

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
