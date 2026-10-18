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

在 GitHub 仓库 Settings → Pages 中将 Source 设置为 **GitHub Actions**。推送到 `main` 后，工作流严格构建并部署到 GitHub Pages。本地构建不会自动发布。
