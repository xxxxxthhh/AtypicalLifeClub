# Atypical Life Club Blog

一个使用 Hugo 构建、部署在 Cloudflare Pages 的个人静态博客。

## 🚀 快速开始

### 本地开发

```bash
# 启动本地开发服务器（包含草稿）
hugo server -D

# 仅正式文章
hugo server
```

访问 [http://localhost:1313](http://localhost:1313) 查看博客。

### 新建文章

```bash
hugo new posts/my-new-post.md
```

然后编辑 `content/posts/my-new-post.md`。

### 文章格式

```markdown
---
title: "文章标题"
date: 2026-01-03T15:55:00+08:00
draft: false           # true 表示草稿，不会发布
tags: ["标签1", "标签2"]
categories: ["分类"]
description: "文章描述"
cover:
    image: "/images/cover.jpg"  # 可选封面图
    alt: "封面图描述"
---

文章正文...
```

### 添加图片

将图片放入 `static/images/` 目录，然后在文章中引用：

```markdown
![图片描述](/images/your-image.jpg)
```

## 📁 项目结构

```
.
├── content/
│   ├── posts/          # 博客文章
│   ├── archives.md     # 归档页面
│   └── search.md       # 搜索页面
├── static/
│   ├── images/         # 静态图片资源
│   ├── invest/         # Invest 工作台（/invest/）
│   │   ├── research/   # 研究中心（/invest/research/）
│   │   └── currency/   # 汇率看板（/invest/currency/）
│   ├── research/       # 旧路径兼容跳转（-> /invest/research/）
│   ├── currency/       # 旧路径兼容跳转（-> /invest/currency/）
│   └── shared/         # 跨模块共享脚本
├── .github/workflows/
│   └── update-currency-data.yml # 汇率数据自动更新
├── themes/
│   └── PaperMod/       # 主题（作为 Git submodule）
├── hugo.toml           # Hugo 配置文件
└── public/             # 构建产物（由 CI 生成，已 gitignore）
```

## 🧩 模块说明

- `/`：主博客（Hugo + PaperMod）
- `/invest/`：Invest 统一入口（研究与追踪模块导航）
- `/invest/research/`：研究中心（数据源 `static/invest/research/data/reports.json`）
- `/invest/currency/`：汇率看板（数据源 `static/invest/currency/data/historical.json`）
- `/research/`、`/currency/`：兼容旧链接，自动重定向到 Invest 子路径

## 🤖 Agent 操作手册（重点）

下面是给后续 agent 的最小可执行流程。

### A. 更新研究报告（推荐流程）

1. 新增或更新 Markdown 正文  
   文件位置：`static/invest/research/*.md`
2. 更新首页卡片元数据  
   文件位置：`static/invest/research/data/reports.json`  
   字段至少包括：`id`、`company`、`ticker`、`title`、`titleEn`、`summary`、`category`、`date`、`lastUpdate`、`file`、`markdownFiles`、`tags`
   - `file` 统一写：`/invest/research/reports/view.html?id=<id>`
   - `markdownFiles` 统一写：`{ "zh": "/invest/research/<zh-report>.md", "en": "/invest/research/<en-report>.md" }`
3. 本地验证  
   ```bash
   python3 static/invest/research/validate_reports.py
   hugo server -D
   ```
   检查：
   - `http://localhost:1313/invest/research/` 卡片和筛选是否正常
   - 新报告详情页是否可打开并正确渲染
   - 详情页顶部中/英切换按钮可切换内容
4. 提交并推送

### B. 更新汇率模块（手动）

```bash
python3 static/invest/currency/update_real_data.py
python3 static/invest/currency/validate_data.py
```

- `update_real_data.py`：拉取最新数据并按日期 upsert 到 `data/historical.json`
- `validate_data.py`：校验 schema、日期顺序、货币字段完整性（失败则不要提交）

### C. 汇率模块（自动）

- 工作流：`.github/workflows/update-currency-data.yml`
- 触发：每天 UTC `00:00`（北京时间 `08:00`）+ 手动触发
- 流程：更新数据 -> 校验数据 -> 仅在有变更时自动提交

### D. 共用前端约束

- 主题切换统一使用：`/shared/theme-switcher.js`
- 不要再复制新的 `theme-switcher.js` 到业务目录
- 静态子应用资源路径统一使用绝对路径（如 `/invest/research/...`、`/invest/currency/...`）

### E. 本地质量检查（提交前）

```bash
# 研究中心元数据校验
python3 static/invest/research/validate_reports.py

# 汇率数据校验
python3 static/invest/currency/validate_data.py

# 前端冒烟（需先启动 hugo server -D）
npm install --no-save playwright
npx playwright install chromium
node scripts/smoke-playwright.js
```

## ☁️ 部署到 Cloudflare Pages

### 1. 推送到 GitHub

```bash
git add .
git commit -m "Initial commit: Hugo blog with PaperMod theme"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. 配置 Cloudflare Pages

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. 进入 **Workers & Pages** > **Create application** > **Pages**
3. 选择 **Connect to Git** > 授权 GitHub
4. 选择你的仓库
5. 配置构建设置：
   - **Framework preset**: `Hugo`
   - **Build command**: `hugo`
   - **Build output directory**: `public`
   - **Environment variables**:
     - `HUGO_VERSION`: `0.154.2`（或更高版本）
6. 点击 **Save and Deploy**

### 3. 绑定自定义域名

1. 部署成功后，进入项目设置
2. 选择 **Custom domains** > **Set up a custom domain**
3. 输入你的域名（需要已在 Cloudflare 托管）
4. Cloudflare 会自动配置 DNS 和 HTTPS

## 🔧 自定义配置

编辑 `hugo.toml` 来自定义博客：

- `baseURL`: 部署后替换为你的域名
- `title`: 博客标题
- `params.description`: 博客描述
- `params.socialIcons`: 社交媒体链接
- `menu.main`: 导航菜单

## 📖 主题文档

PaperMod 主题详细文档：[https://adityatelange.github.io/hugo-PaperMod/](https://adityatelange.github.io/hugo-PaperMod/)

## 📝 发布流程

1. 本地编写 Markdown 文章
2. `hugo server -D` 预览效果
3. 将 `draft: true` 改为 `draft: false`
4. `git add . && git commit -m "新文章：xxx"`
5. `git push` - Cloudflare Pages 自动构建发布

## 📄 License

MIT
