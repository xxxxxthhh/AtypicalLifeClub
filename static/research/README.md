# Research Hub - 研报聚合平台

专业投资研究报告聚合平台，追踪关注公司的最新动态，提供深度投资研究分析。

## 项目简介

Research Hub 是一个基于 GitHub Pages 的静态网站，用于展示和管理投资研究报告。网站采用现代化的响应式设计，支持移动端访问，提供优雅的阅读体验。

## 功能特点

- ✅ **响应式设计**：完美支持桌面端和移动端
- ✅ **研报列表**：卡片式展示，支持分类筛选
- ✅ **详情页面**：自动生成目录，支持平滑滚动
- ✅ **Markdown 支持**：研报使用 Markdown 格式，易于编辑和维护
- ✅ **打印友好**：支持打印输出，适合离线阅读
- ✅ **快速加载**：静态网站，加载速度快

## 项目结构

```
research-hub/
├── index.html              # 首页
├── styles.css              # 首页样式
├── app.js                  # 首页交互逻辑
├── report-style.css        # 报告详情页样式
├── reports/                # 报告 HTML 文件目录
│   └── oklo-2026.html     # OKLO 报告详情页
├── OKLO_研究报告_2026.md  # OKLO 报告 Markdown 源文件
└── README.md              # 项目说明文档
```

## 如何添加新报告

### 1. 准备 Markdown 文件

将研报以 Markdown 格式保存到项目根目录，例如：`公司名_研究报告_日期.md`

### 2. 更新 app.js

在 `app.js` 的 `reports` 数组中添加新报告信息：

```javascript
{
    id: 'company-2026',
    company: '公司名称',
    ticker: '股票代码',
    title: '报告标题',
    summary: '报告摘要',
    tags: ['标签1', '标签2'],
    category: 'tech', // 分类：nuclear, tech, energy 等
    date: '2026-02-03',
    lastUpdate: '2026-02-03',
    file: 'reports/company-2026.html',
    highlights: [
        '要点1',
        '要点2'
    ]
}
```

### 3. 创建报告详情页

复制 `reports/oklo-2026.html` 并修改：
- 更新标题和元信息
- 修改 Markdown 文件路径

### 4. 提交更新

```bash
git add .
git commit -m "Add new report: 公司名"
git push origin main
```

## 部署到 GitHub Pages

### 首次部署

1. 在 GitHub 创建新仓库（例如：`research-hub`）

2. 推送代码到 GitHub：
```bash
cd /workspace/group/research-hub
git remote add origin https://github.com/你的用户名/research-hub.git
git branch -M main
git push -u origin main
```

3. 在 GitHub 仓库设置中启用 GitHub Pages：
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / (root)
   - Save

4. 等待几分钟后，访问：`https://你的用户名.github.io/research-hub/`

### 更新报告

每次更新报告后，只需：
```bash
git add .
git commit -m "Update report: 描述"
git push
```

GitHub Pages 会自动重新部署。

## 定期更新流程

### 1. 审查现有报告
- 检查公司最新动态
- 更新财务数据
- 调整投资建议

### 2. 更新 Markdown 文件
- 修改对应的 `.md` 文件
- 更新日期和版本信息

### 3. 更新元数据
- 在 `app.js` 中更新 `lastUpdate` 字段
- 如有需要，更新摘要和要点

### 4. 提交并部署
```bash
git add .
git commit -m "Update: OKLO 报告 - 添加Q1财报分析"
git push
```

## 技术栈

- **HTML5/CSS3**：现代化的网页结构和样式
- **JavaScript (ES6+)**：交互逻辑
- **Marked.js**：Markdown 渲染
- **Google Fonts**：Inter 和 Noto Sans SC 字体
- **GitHub Pages**：免费静态网站托管

## 浏览器支持

- Chrome/Edge (最新版本)
- Firefox (最新版本)
- Safari (最新版本)
- 移动端浏览器

## 许可证

本项目仅供个人研究使用，报告内容不构成投资建议。

---

*最后更新：2026年2月3日*
