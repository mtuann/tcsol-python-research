(function () {
  function setLanguage(lang) {
    document.body.dataset.lang = lang;
    document.documentElement.lang = lang;
    document.querySelectorAll(".lang-button, .language-switcher button").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.lang === lang));
    });
  }

  window.CourseModule = {
    setLanguage
  };

  document.addEventListener("DOMContentLoaded", () => {
    const initial = document.body.dataset.lang || document.documentElement.lang || "vi";
    setLanguage(initial);
    document.querySelectorAll(".lang-button, .language-switcher button").forEach((button) => {
      if (!button.dataset.lang) return;
      button.addEventListener("click", () => setLanguage(button.dataset.lang));
    });
  });
}());
