// 主题切换逻辑 - 与博客同步
(function() {
    'use strict';

    // 初始化主题
    function initTheme() {
        // 从 localStorage 读取主题设置（与博客共享）
        const theme = localStorage.getItem('pref-theme') || 'light';
        
        // 应用主题
        if (theme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
            document.body.classList.add('dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            document.body.classList.remove('dark');
        }
        
        console.log('Theme initialized:', theme);
    }

    // 监听 localStorage 变化（跨标签页同步）
    window.addEventListener('storage', function(e) {
        if (e.key === 'pref-theme') {
            initTheme();
        }
    });

    // 页面加载时初始化
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTheme);
    } else {
        initTheme();
    }

    // 添加主题切换按钮（可选）
    function addThemeToggle() {
        const navbar = document.querySelector('.navbar .container');
        if (!navbar) return;

        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'theme-toggle';
        toggleBtn.innerHTML = '🌓';
        toggleBtn.title = '切换主题';
        toggleBtn.style.cssText = 'background: none; border: none; font-size: 1.5rem; cursor: pointer; padding: 0.5rem;';
        
        toggleBtn.addEventListener('click', function() {
            const currentTheme = localStorage.getItem('pref-theme') || 'light';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            localStorage.setItem('pref-theme', newTheme);
            initTheme();
        });

        navbar.appendChild(toggleBtn);
    }

    // 页面加载完成后添加切换按钮
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', addThemeToggle);
    } else {
        addThemeToggle();
    }
})();
