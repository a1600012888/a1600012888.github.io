async function loadText(url) {
  const res = await fetch(url, { cache: "no-cache" });
  if (!res.ok) throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  return await res.text();
}

function getEmbeddedMarkdown() {
  const node = document.getElementById("embedded-markdown");
  if (!node) return null;
  const text = (node.textContent || "").trim();
  return text.length ? text : null;
}

function normalizeObsidianImageLinks(md) {
  // Converts Obsidian-style embedded links like ![x](:/hash.png) into plain text
  // so the page doesn't show broken images. You can replace them with local files.
  return md.replace(/!\[([^\]]*)\]\(:\/[^)]+\)/g, (_m, alt) => `**[missing image: ${alt || "image"}]**`);
}

function configureMarked() {
  const hasHljs = typeof window.hljs !== "undefined";
  marked.setOptions({
    gfm: true,
    breaks: false,
    headerIds: true,
    mangle: false,
    highlight(code, lang) {
      if (!hasHljs) return code;
      if (lang && window.hljs.getLanguage(lang))
        return window.hljs.highlight(code, { language: lang }).value;
      return window.hljs.highlightAuto(code).value;
    },
  });
}

async function render() {
  const el = document.getElementById("content");
  try {
    configureMarked();
    let raw = null;

    // If opened as file://, browsers often block fetch() for local sibling files.
    if (window.location.protocol === "file:") {
      raw = getEmbeddedMarkdown();
      if (!raw) {
        throw new Error(
          "You opened this page as a local file (file://...), so the browser blocks loading post.md. " +
            "Preview via a local server instead, e.g. run: `python3 -m http.server 8000` from the repo root, " +
            "then open http://localhost:8000/blogs/rnn_memory/ .",
        );
      }
    } else {
      raw = await loadText("./post.md");
    }

    const md = normalizeObsidianImageLinks(raw);
    el.classList.remove("loading");
    el.innerHTML = marked.parse(md);

    // Highlight after insertion (for fenced blocks without language).
    if (typeof window.hljs !== "undefined") {
      document.querySelectorAll("pre code").forEach((block) => window.hljs.highlightElement(block));
    }

    // Typeset math after render.
    if (window.MathJax?.typesetPromise) await window.MathJax.typesetPromise([el]);
  } catch (err) {
    el.classList.remove("loading");
    el.innerHTML = `<div class="error"><strong>Error:</strong> ${String(err.message || err)}</div>`;
  }
}

render();

