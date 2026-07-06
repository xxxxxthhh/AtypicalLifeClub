// Shared zh/en language-switch persistence, used by invest/app.js and research/coverage-map.html
const LANG_QUERY_KEY = "lang";
const LANG_STORAGE_KEY = "invest_home_lang";
const SUPPORTED_LANGS = ["zh", "en"];

function normalizeLanguage(value) {
    const lang = String(value || "").toLowerCase();
    return SUPPORTED_LANGS.includes(lang) ? lang : "";
}

function chooseInitialLanguage() {
    const params = new URLSearchParams(window.location.search);
    const fromQuery = normalizeLanguage(params.get(LANG_QUERY_KEY));
    if (fromQuery) return fromQuery;

    try {
        const fromStorage = normalizeLanguage(window.localStorage.getItem(LANG_STORAGE_KEY));
        if (fromStorage) return fromStorage;
    } catch (error) {
        // localStorage may be unavailable in private or restricted browser contexts.
    }

    return "en";
}

function saveLanguage(lang) {
    try {
        window.localStorage.setItem(LANG_STORAGE_KEY, lang);
    } catch (error) {
        // localStorage may be unavailable in private or restricted browser contexts.
    }
}

function syncLanguageQuery(lang) {
    const params = new URLSearchParams(window.location.search);
    params.set(LANG_QUERY_KEY, lang);
    window.history.replaceState({}, "", `${window.location.pathname}?${params.toString()}`);
}

function renderLanguageSwitchUI(currentLang) {
    const root = document.getElementById("languageSwitch");
    if (!root) return;

    root.querySelectorAll(".lang-opt").forEach((button) => {
        const active = button.dataset.lang === currentLang;
        button.classList.toggle("active", active);
        button.setAttribute("aria-pressed", active ? "true" : "false");
    });
}
