// Backward-compat shim: old path kept for cached pages.
(function () {
    var s = document.createElement('script');
    s.src = '/shared/theme-switcher.js';
    document.head.appendChild(s);
})();
