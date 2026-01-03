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
│   └── images/         # 静态图片资源
├── themes/
│   └── PaperMod/       # 主题（作为 Git submodule）
├── hugo.toml           # Hugo 配置文件
└── public/             # 构建产物（由 CI 生成，已 gitignore）
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
