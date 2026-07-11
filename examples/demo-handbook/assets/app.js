(() => {
  "use strict";
  const root = document.documentElement;
  const body = document.body;
  const base = window.__HANDBOOK_BASE__ || "";
  const index = Array.isArray(window.__HANDBOOK_SEARCH__) ? window.__HANDBOOK_SEARCH__ : [];
  const themeButton = document.querySelector("[data-theme-toggle]");
  const menuButton = document.querySelector("[data-menu-toggle]");
  const sidebar = document.getElementById("sidebar");
  const dialog = document.querySelector(".search-dialog");
  const input = document.getElementById("search-input");
  const results = document.querySelector(".search-results");
  let selected = -1;

  function preferredTheme() {
    const saved = localStorage.getItem("handbook-theme");
    if (saved === "light" || saved === "dark") return saved;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  function setTheme(value) {
    root.dataset.theme = value;
    localStorage.setItem("handbook-theme", value);
    if (themeButton) themeButton.setAttribute("aria-label", value === "dark" ? "切换到浅色主题" : "切换到深色主题");
  }
  setTheme(preferredTheme());
  if (themeButton) themeButton.addEventListener("click", () => setTheme(root.dataset.theme === "dark" ? "light" : "dark"));

  function closeMenu() {
    body.classList.remove("menu-open");
    if (menuButton) menuButton.setAttribute("aria-expanded", "false");
  }
  if (menuButton) menuButton.addEventListener("click", () => {
    const open = body.classList.toggle("menu-open");
    menuButton.setAttribute("aria-expanded", String(open));
  });
  document.querySelectorAll("[data-menu-close], .nav-link").forEach((x) => x.addEventListener("click", closeMenu));

  if (sidebar) {
    const saved = sessionStorage.getItem("handbook-sidebar-scroll");
    if (saved !== null) sidebar.scrollTop = Number(saved) || 0;
    const active = sidebar.querySelector(".nav-link.current");
    if (active && saved === null) active.scrollIntoView({ block: "center" });
    sidebar.addEventListener("scroll", () => sessionStorage.setItem("handbook-sidebar-scroll", String(sidebar.scrollTop)), { passive: true });
  }

  function normalize(value) { return value.toLocaleLowerCase().normalize("NFKC"); }
  function score(item, terms) {
    const fields = [normalize(item.title || ""), normalize(item.section || ""), normalize(item.summary || ""), normalize(item.text || "")];
    let total = 0;
    for (const term of terms) {
      if (!fields.some((field) => field.includes(term))) return 0;
      total += fields[0].includes(term) ? 10 : 0;
      total += fields[1].includes(term) ? 5 : 0;
      total += fields[2].includes(term) ? 4 : 0;
      total += fields[3].includes(term) ? 1 : 0;
    }
    return total;
  }
  function renderSearch() {
    if (!results || !input) return;
    const terms = normalize(input.value).split(/\s+/).filter(Boolean);
    selected = -1;
    results.replaceChildren();
    if (!terms.length) {
      const hint = document.createElement("p"); hint.className = "search-empty"; hint.textContent = "输入关键词开始搜索。"; results.append(hint); return;
    }
    const matches = index.map((item) => ({ item, rank: score(item, terms) })).filter((x) => x.rank > 0).sort((a,b) => b.rank-a.rank).slice(0,12);
    if (!matches.length) {
      const empty = document.createElement("p"); empty.className = "search-empty"; empty.textContent = "没有找到匹配页面。"; results.append(empty); return;
    }
    for (const { item } of matches) {
      const link = document.createElement("a"); link.className = "search-result"; link.href = base + item.url;
      const title = document.createElement("strong"); title.textContent = item.title;
      const meta = document.createElement("span"); meta.textContent = `${item.section} · ${item.summary}`;
      link.append(title, meta); results.append(link);
    }
  }
  function openSearch() {
    if (!dialog || !input) return;
    dialog.hidden = false; body.style.overflow = "hidden"; renderSearch(); requestAnimationFrame(() => input.focus());
  }
  function closeSearch() { if (!dialog) return; dialog.hidden = true; body.style.overflow = ""; selected = -1; }
  function selectResult(delta) {
    if (!results) return;
    const links = Array.from(results.querySelectorAll(".search-result"));
    if (!links.length) return;
    selected = (selected + delta + links.length) % links.length;
    links.forEach((x,i) => x.classList.toggle("selected", i === selected));
    links[selected].scrollIntoView({ block: "nearest" });
  }
  document.querySelectorAll("[data-search-open]").forEach((x) => x.addEventListener("click", openSearch));
  document.querySelectorAll("[data-search-close]").forEach((x) => x.addEventListener("click", closeSearch));
  if (dialog) dialog.addEventListener("click", (event) => { if (event.target === dialog) closeSearch(); });
  if (input) input.addEventListener("input", renderSearch);
  document.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") { event.preventDefault(); openSearch(); return; }
    if (!dialog || dialog.hidden) return;
    if (event.key === "Escape") closeSearch();
    if (event.key === "ArrowDown") { event.preventDefault(); selectResult(1); }
    if (event.key === "ArrowUp") { event.preventDefault(); selectResult(-1); }
    if (event.key === "Enter" && selected >= 0 && results) {
      const target = results.querySelectorAll(".search-result")[selected]; if (target) target.click();
    }
  });

  const progress = document.querySelector("[data-progress]");
  function updateProgress() {
    if (!progress) return;
    const available = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = `${available > 0 ? Math.min(100, Math.max(0, window.scrollY / available * 100)) : 0}%`;
  }
  updateProgress(); window.addEventListener("scroll", updateProgress, { passive: true });

  const tocLinks = Array.from(document.querySelectorAll(".page-toc a"));
  if (tocLinks.length && "IntersectionObserver" in window) {
    const byId = new Map(tocLinks.map((x) => [decodeURIComponent(x.hash.slice(1)), x]));
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((x) => x.isIntersecting).sort((a,b) => a.boundingClientRect.top-b.boundingClientRect.top);
      if (!visible.length) return;
      tocLinks.forEach((x) => x.classList.remove("active"));
      const current = byId.get(visible[0].target.id); if (current) current.classList.add("active");
    }, { rootMargin: "-76px 0px -70% 0px", threshold: [0,1] });
    byId.forEach((_,id) => { const heading = document.getElementById(id); if (heading) observer.observe(heading); });
  }

  document.querySelectorAll("pre > code").forEach((code) => {
    const pre = code.parentElement; if (!pre || pre.classList.contains("mermaid")) return;
    const button = document.createElement("button"); button.type = "button"; button.className = "copy-button"; button.textContent = "复制";
    button.addEventListener("click", async () => {
      try { await navigator.clipboard.writeText(code.textContent || ""); button.textContent = "已复制"; setTimeout(() => { button.textContent = "复制"; }, 1400); }
      catch (_) { button.textContent = "复制失败"; }
    });
    pre.append(button);
  });
  if (window.mermaid && document.querySelector(".mermaid")) window.mermaid.initialize({ startOnLoad: true, securityLevel: "strict", theme: root.dataset.theme === "dark" ? "dark" : "default" });
})();
