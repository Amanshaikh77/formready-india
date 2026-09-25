with open("docs/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace CSS absolute positioning with a clean relative top bar
old_css_needle = ".top-mode-bar {"
new_top_css = """
    .top-mode-bar {
      width: 100%;
      display: flex;
      justify-content: flex-start;
      align-items: center;
      margin-bottom: 8px;
      z-index: 100;
    }
"""

if old_css_needle in html:
    # replace block up to z-index: 1000; }
    import re
    html = re.sub(r'\.top-mode-bar\s*\{[^}]*\}', new_top_css.strip(), html)

# Make sure header has clean spacing and no negative margins
html = html.replace('padding-top: 24px;', 'padding-top: 6px;')

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Homepage toggle overlap fixed!")
