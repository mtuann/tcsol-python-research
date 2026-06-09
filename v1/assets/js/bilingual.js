(function () {
  const STORAGE_KEY = "tcsol-python-lang";
  let translations = {};
  let currentLang = "vi";
  let fallbackLang = "vi";
  let onChange = null;

  function hasLang(lang) {
    return Boolean(lang && translations[lang]);
  }

  function getStoredLang() {
    try {
      return window.localStorage.getItem(STORAGE_KEY);
    } catch (error) {
      return null;
    }
  }

  function storeLang(lang) {
    try {
      window.localStorage.setItem(STORAGE_KEY, lang);
    } catch (error) {
      /* localStorage may be unavailable in strict browser settings. */
    }
  }

  function lookup(key, lang) {
    if (!key || !translations[lang]) return undefined;
    return translations[lang][key];
  }

  function t(key, fallback) {
    const value = lookup(key, currentLang);
    if (value !== undefined) return value;
    const fallbackValue = lookup(key, fallbackLang);
    if (fallbackValue !== undefined) return fallbackValue;
    return fallback !== undefined ? fallback : key;
  }

  function setAttrFromKey(selector, attr) {
    document.querySelectorAll(selector).forEach((element) => {
      const key = element.dataset[attr.key];
      const value = t(key, "");
      if (value !== "") element.setAttribute(attr.name, value);
    });
  }

  function applyTranslations() {
    document.documentElement.lang = currentLang;

    document.querySelectorAll("[data-i18n]").forEach((element) => {
      element.textContent = t(element.dataset.i18n, element.textContent);
    });

    document.querySelectorAll("[data-i18n-html]").forEach((element) => {
      element.innerHTML = t(element.dataset.i18nHtml, element.innerHTML);
    });

    setAttrFromKey("[data-i18n-aria-label]", { key: "i18nAriaLabel", name: "aria-label" });
    setAttrFromKey("[data-i18n-title]", { key: "i18nTitle", name: "title" });
    setAttrFromKey("[data-i18n-placeholder]", { key: "i18nPlaceholder", name: "placeholder" });
    setAttrFromKey("[data-i18n-alt]", { key: "i18nAlt", name: "alt" });

    document.querySelectorAll("[data-lang-option]").forEach((button) => {
      const isActive = button.dataset.langOption === currentLang;
      button.setAttribute("aria-pressed", String(isActive));
    });
  }

  function setLang(lang, options) {
    if (!hasLang(lang)) lang = fallbackLang;
    currentLang = lang;
    applyTranslations();
    if (!options || options.persist !== false) storeLang(lang);
    if (typeof onChange === "function") onChange(lang, t);
    window.dispatchEvent(new CustomEvent("bilingual:change", { detail: { lang } }));
  }

  function bindLanguageButtons() {
    document.querySelectorAll("[data-lang-option]").forEach((button) => {
      button.addEventListener("click", () => setLang(button.dataset.langOption));
    });
  }

  function init(options) {
    translations = options.translations || {};
    fallbackLang = options.defaultLang || "vi";
    onChange = options.onChange || null;
    bindLanguageButtons();
    const requested = getStoredLang() || fallbackLang;
    setLang(hasLang(requested) ? requested : fallbackLang, { persist: false });
  }

  window.Bilingual = {
    init,
    setLang,
    getLang: () => currentLang,
    t
  };
})();
