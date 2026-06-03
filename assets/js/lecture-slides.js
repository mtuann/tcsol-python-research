(function () {
  function titleInfo(section) {
    const heading = section.querySelector("h1, h2");
    if (!heading) return { text: "Slide", key: null, htmlKey: null };
    return {
      text: heading.textContent.trim(),
      html: heading.innerHTML,
      key: heading.dataset.i18n || null,
      htmlKey: heading.dataset.i18nHtml || null
    };
  }

  function init() {
    const sections = Array.from(document.querySelectorAll(".slides > section"));
    let current = 0;
    let lastFocusBeforeOverview = null;
    let isUpdatingHash = false;

    const nav = document.createElement("nav");
    nav.className = "fallback-nav";
    nav.setAttribute("aria-label", "Slide navigation");
    nav.setAttribute("data-i18n-aria-label", "nav.slides.aria");
    nav.innerHTML = `
      <button type="button" data-dir="-1" data-i18n="nav.previous">Previous</button>
      <span class="slide-counter"></span>
      <form class="slide-jump" aria-label="Go to slide" data-i18n-aria-label="nav.jump.aria">
        <label for="slide-jump-input" data-i18n="nav.jump.label">Slide</label>
        <input id="slide-jump-input" type="number" min="1" inputmode="numeric" aria-label="Slide number" data-i18n-aria-label="nav.jump.input">
        <button class="jump-button" type="submit" data-i18n="nav.jump.go">Go</button>
      </form>
      <button type="button" data-dir="1" data-i18n="nav.next">Next</button>
      <button class="nav-link" type="button" data-toc-open data-i18n="nav.toc">Overview</button>
      <a class="nav-link" href="./" data-i18n="nav.week">Week</a>
    `;
    document.body.appendChild(nav);

    const overview = document.createElement("aside");
    overview.className = "slide-overview";
    overview.setAttribute("aria-hidden", "true");
    overview.innerHTML = `
      <div class="overview-panel" role="dialog" aria-modal="true" aria-label="Slide overview" data-i18n-aria-label="nav.toc.title">
        <div class="overview-head">
          <div>
            <span class="tag" data-i18n="nav.toc">Overview</span>
            <h2 data-i18n="nav.toc.title">Slide overview</h2>
            <p class="lead" data-i18n="nav.toc.hint">Choose a section to jump directly to the slide you need.</p>
          </div>
          <button class="overview-close" type="button" data-toc-close data-i18n-aria-label="nav.toc.close" aria-label="Close">&times;</button>
        </div>
        <div class="overview-grid"></div>
      </div>
    `;
    document.body.appendChild(overview);

    const label = nav.querySelector(".slide-counter");
    const input = nav.querySelector("#slide-jump-input");
    const prev = nav.querySelector('[data-dir="-1"]');
    const next = nav.querySelector('[data-dir="1"]');
    const overviewGrid = overview.querySelector(".overview-grid");

    sections.forEach((section, idx) => {
      const info = titleInfo(section);
      const button = document.createElement("button");
      button.className = "toc-item";
      button.type = "button";
      button.dataset.slideTarget = String(idx);
      const titleAttr = info.htmlKey ? `data-i18n-html="${info.htmlKey}"` : info.key ? `data-i18n="${info.key}"` : "";
      button.innerHTML = `
        <span class="toc-index">${String(idx + 1).padStart(2, "0")}</span>
        <span class="toc-title" ${titleAttr}>${info.htmlKey ? info.html : info.text}</span>
      `;
      overviewGrid.appendChild(button);
    });

    const tocButtons = Array.from(overviewGrid.querySelectorAll(".toc-item"));

    function setOverview(open) {
      if (open) lastFocusBeforeOverview = document.activeElement;
      overview.classList.toggle("is-open", open);
      overview.setAttribute("aria-hidden", String(!open));
      if (open) {
        const activeButton = overviewGrid.querySelector(".toc-item.active");
        if (activeButton) activeButton.focus();
      } else if (lastFocusBeforeOverview && typeof lastFocusBeforeOverview.focus === "function") {
        lastFocusBeforeOverview.focus();
      }
    }

    function show(index, options) {
      current = Math.max(0, Math.min(sections.length - 1, index));
      sections.forEach((section, idx) => section.classList.toggle("active", idx === current));
      tocButtons.forEach((button, idx) => {
        const isActive = idx === current;
        button.classList.toggle("active", isActive);
        if (isActive) button.setAttribute("aria-current", "true");
        else button.removeAttribute("aria-current");
      });
      label.textContent = (current + 1) + " / " + sections.length;
      input.max = String(sections.length);
      input.value = String(current + 1);
      prev.disabled = current === 0;
      next.disabled = current === sections.length - 1;
      if (!options || options.updateHash !== false) {
        isUpdatingHash = true;
        location.hash = "slide-" + (current + 1);
        window.setTimeout(() => {
          isUpdatingHash = false;
        }, 0);
      }
    }

    document.addEventListener("click", (event) => {
      if (event.target.closest("[data-toc-open]")) setOverview(true);
      if (event.target.closest("[data-toc-close]")) setOverview(false);
      if (event.target === overview) setOverview(false);
    });

    overviewGrid.addEventListener("click", (event) => {
      const button = event.target.closest(".toc-item");
      if (!button) return;
      show(Number(button.dataset.slideTarget));
      setOverview(false);
    });

    nav.addEventListener("click", (event) => {
      const button = event.target.closest("button[data-dir]");
      if (!button) return;
      show(current + Number(button.dataset.dir));
    });

    nav.querySelector(".slide-jump").addEventListener("submit", (event) => {
      event.preventDefault();
      const target = Number(input.value);
      if (Number.isFinite(target)) show(target - 1);
    });

    window.addEventListener("keydown", (event) => {
      if (event.target && ["INPUT", "TEXTAREA", "BUTTON", "A", "SELECT"].includes(event.target.tagName)) return;
      if (event.key === "Escape") setOverview(false);
      if (overview.classList.contains("is-open")) return;
      if (event.key === "ArrowRight" || event.key === " ") show(current + 1);
      if (event.key === "ArrowLeft") show(current - 1);
    });

    window.addEventListener("hashchange", () => {
      if (isUpdatingHash) return;
      const match = location.hash.match(/slide-(\d+)/);
      if (match) show(Number(match[1]) - 1, { updateHash: false });
    });

    const hashMatch = location.hash.match(/slide-(\d+)/);
    show(hashMatch ? Number(hashMatch[1]) - 1 : 0);

    if (window.Bilingual && typeof window.Bilingual.setLang === "function") {
      window.Bilingual.setLang(window.Bilingual.getLang(), { persist: false });
    }
  }

  window.LectureSlides = { init };
})();
