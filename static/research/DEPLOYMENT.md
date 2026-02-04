# 部署指南 - Research Hub

## 项目已创建成功！

GitHub 仓库：https://github.com/xxxxxthhh/research-hub

## 部署步骤

### 方法一：使用 GitHub 网页界面上传（推荐）

1. **访问仓库**
   - 打开：https://github.com/xxxxxthhh/research-hub

2. **上传文件**
   - 点击 "Add file" → "Upload files"
   - 将以下文件拖拽上传：
     - index.html
     - styles.css
     - app.js
     - report-style.css
     - README.md
     - .gitignore
     - OKLO_研究报告_2026.md
   - 创建 `reports` 文件夹并上传 `oklo-2026.html`
   - 创建 `.github` 文件夹并上传 `README.md`

3. **提交更改**
   - 填写提交信息："Initial commit: Research Hub"
   - 点击 "Commit changes"

4. **启用 GitHub Pages**
   - 进入仓库 Settings → Pages
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)
   - 点击 Save

5. **等待部署**
   - 等待 2-3 分钟
   - 访问：https://xxxxxthhh.github.io/research-hub/

### 方法二：使用命令行（如果你有 Git 访问权限）

```bash
cd /workspace/group/research-hub

# 添加远程仓库
git remote add origin https://github.com/xxxxxthhh/research-hub.git

# 推送代码
git push -u origin main

# 启用 GitHub Pages
gh api repos/xxxxxthhh/research-hub/pages -X POST \
  -f source[branch]=main -f source[path]=/
```

## 项目文件说明

### 核心文件
- `index.html` - 首页
- `styles.css` - 首页样式
- `app.js` - 首页交互逻辑
- `report-style.css` - 报告详情页样式

### 报告文件
- `OKLO_研究报告_2026.md` - OKLO 报告 Markdown 源文件
- `reports/oklo-2026.html` - OKLO 报告详情页

### 文档
- `README.md` - 项目说明
- `.github/README.md` - GitHub 仓库说明

## 添加新报告的步骤

### 1. 准备 Markdown 文件
将新报告保存为 `.md` 文件到项目根目录

### 2. 更新 app.js
在 `reports` 数组中添加新报告信息：

```javascript
{
    id: 'company-2026',
    company: '公司名称',
    ticker: '股票代码',
    title: '报告标题',
    summary: '报告摘要（1-2句话）',
    tags: ['标签1', '标签2', '标签3'],
    category: 'tech', // nuclear, tech, energy 等
    date: '2026-02-03',
    lastUpdate: '2026-02-03',
    file: 'reports/company-2026.html',
    highlights: [
        '核心要点1',
        '核心要点2',
        '核心要点3'
    ]
}
```

### 3. 创建报告详情页
复制 `reports/oklo-2026.html` 并修改：
- 更新 `<title>` 标签
- 修改报告标题和元信息
- 更新 Markdown 文件路径（fetch 函数中）

### 4. 上传到 GitHub
- 通过网页界面上传新文件
- 或使用 Git 命令推送

## 定期更新报告

### 更新现有报告
1. 修改对应的 `.md` 文件
2. 在 `app.js` 中更新 `lastUpdate` 字段
3. 提交并推送到 GitHub

### 审查周期建议
- 季度财报后：更新财务数据
- 重大事件后：更新项目进展
- 每月一次：检查行业动态

## 网站访问

部署成功后，访问：
**https://xxxxxthhh.github.io/research-hub/**

## 需要帮助？

如果遇到问题，可以：
1. 查看 GitHub Pages 部署日志
2. 检查浏览器控制台错误
3. 确认所有文件路径正确

---

*创建日期：2026年2月3日*
