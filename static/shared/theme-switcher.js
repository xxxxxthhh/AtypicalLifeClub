// Shared theme switch logic - synced with PaperMod "pref-theme"
(function () {
    'use strict';

    function initTheme() {
        const theme = localStorage.getItem('pref-theme') || 'light';

        if (theme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
            document.body.classList.add('dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            document.body.classList.remove('dark');
        }
    }

    function addThemeToggle() {
        const navbar = document.querySelector('.navbar .container');
        if (!navbar || navbar.querySelector('.theme-toggle')) return;

        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'theme-toggle';
        toggleBtn.innerHTML = '🌓';
        toggleBtn.title = '切换主题';
        toggleBtn.style.cssText =
            'background: none; border: none; font-size: 1.5rem; cursor: pointer; padding: 0.5rem;';

        toggleBtn.addEventListener('click', function () {
            const currentTheme = localStorage.getItem('pref-theme') || 'light';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            localStorage.setItem('pref-theme', newTheme);
            initTheme();
        });

        navbar.appendChild(toggleBtn);
    }

    window.addEventListener('storage', function (e) {
        if (e.key === 'pref-theme') initTheme();
    });

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTheme);
        document.addEventListener('DOMContentLoaded', addThemeToggle);
    } else {
        initTheme();
        addThemeToggle();
    }
})();
