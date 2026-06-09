(function () {
  let slides = [];
  let active = 0;

  function clamp(index) {
    return Math.max(0, Math.min(slides.length - 1, index));
  }

  function show(index) {
    if (!slides.length) return;
    active = clamp(index);
    slides.forEach((slide, i) => slide.classList.toggle("active", i === active));
    const current = document.getElementById("current");
    const jump = document.getElementById("jump");
    if (current) current.textContent = String(active + 1);
    if (jump) jump.value = String(active + 1);
    window.location.hash = `/${active + 1}`;
  }

  function goFromInput() {
    const jump = document.getElementById("jump");
    if (!jump) return;
    const value = Number(jump.value);
    if (Number.isFinite(value)) show(value - 1);
  }

  function setLanguage(lang) {
    document.body.dataset.lang = lang;
    document.documentElement.lang = lang;
    document.querySelectorAll(".lang-button, .language-switcher button").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.lang === lang));
    });
  }

  function buildToc() {
    const tocList = document.getElementById("toc-list");
    const tocPanel = document.getElementById("toc-panel");
    if (!tocList || !tocPanel) return;
    tocList.innerHTML = "";
    slides.forEach((slide, i) => {
      const button = document.createElement("button");
      button.className = "toc-item";
      button.type = "button";
      button.innerHTML = `<span class="toc-number">${i + 1}</span><span class="toc-title">${slide.dataset.title || `Slide ${i + 1}`}</span>`;
      button.addEventListener("click", () => {
        show(i);
        tocPanel.classList.remove("open");
      });
      tocList.appendChild(button);
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    slides = Array.from(document.querySelectorAll(".slide"));
    const total = document.getElementById("total");
    const jump = document.getElementById("jump");
    if (total) total.textContent = String(slides.length);
    if (jump) jump.max = String(slides.length);

    document.getElementById("prev")?.addEventListener("click", () => show(active - 1));
    document.getElementById("next")?.addEventListener("click", () => show(active + 1));
    document.getElementById("go")?.addEventListener("click", goFromInput);
    jump?.addEventListener("keydown", (event) => {
      if (event.key === "Enter") goFromInput();
    });

    const tocPanel = document.getElementById("toc-panel");
    document.getElementById("toc-open")?.addEventListener("click", () => tocPanel?.classList.add("open"));
    document.getElementById("toc-close")?.addEventListener("click", () => tocPanel?.classList.remove("open"));

    document.querySelectorAll(".lang-button, .language-switcher button").forEach((button) => {
      if (!button.dataset.lang) return;
      button.addEventListener("click", () => setLanguage(button.dataset.lang));
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "ArrowRight" || event.key === "PageDown") show(active + 1);
      if (event.key === "ArrowLeft" || event.key === "PageUp") show(active - 1);
      if (event.key.toLowerCase() === "t") tocPanel?.classList.toggle("open");
      if (event.key === "Escape") tocPanel?.classList.remove("open");
    });

    buildToc();
    setLanguage(document.body.dataset.lang || document.documentElement.lang || "vi");
    const match = window.location.hash.match(/#\/(\d+)/);
    show(match ? Number(match[1]) - 1 : 0);
  });
}());
