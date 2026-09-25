file_path = "docs/3d/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# CSS Update for Number + Name Pills
old_css = """.tool-num-btn {
      flex-shrink: 0;
      min-width: 32px;
      height: 28px;
      border-radius: 8px;
      background: rgba(22, 16, 10, 0.85);
      border: 1px solid rgba(245, 166, 35, 0.25);
      color: var(--muted);
      font-family: 'Share Tech Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }"""

new_css = """.tool-num-btn {
      flex-shrink: 0;
      height: 30px;
      padding: 0 12px;
      border-radius: 999px;
      background: rgba(22, 16, 10, 0.85);
      border: 1px solid rgba(245, 166, 35, 0.25);
      color: var(--muted);
      font-family: 'Space Grotesk', sans-serif;
      font-size: 11px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.22s ease;
    }
    .tool-num-btn .pill-num {
      font-family: 'Share Tech Mono', monospace;
      color: var(--amber);
      font-weight: 800;
      font-size: 10.5px;
    }
    .tool-num-btn.active .pill-num {
      color: #040302;
    }"""

if old_css in code:
    code = code.replace(old_css, new_css)

# JS Update to render Number + Name inside button
old_js = """    btn.innerText = i + 1;
    btn.title = tool.name;"""

new_js = """    btn.innerHTML = `<span class="pill-num">#${i + 1}</span> ${tool.name}`;
    btn.title = tool.name;"""

if old_js in code:
    code = code.replace(old_js, new_js)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

with open("3d/index.html", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated pill tracker with Number + Tool Name successfully!")
