import re

file_path = "docs/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Create Inline SVG Favicon
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="16" fill="#14100c"/>
  <rect x="2" y="2" width="60" height="60" rx="14" fill="none" stroke="#f5a623" stroke-width="3"/>
  <path d="M36 10 L18 34 L32 34 L26 54 L46 28 L32 28 Z" fill="#f5a623" filter="drop-shadow(0 0 6px #ffb84d)"/>
</svg>'''

with open("docs/favicon.svg", "w", encoding="utf-8") as f:
    f.write(favicon_svg)

# 2. Meta tags & JSON-LD Schema for Google Search
seo_head_tags = '''
  <!-- Google Search Favicon -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/favicon.svg">

  <!-- Tell Google the exact site name (Replaces 'Render') -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "FormReady India",
    "alternateName": ["FormReady", "India Form Ready"],
    "url": "https://formready-india.onrender.com/"
  }
  </script>
'''

# Inject right after <head>
if "application/ld+json" not in html:
    html = html.replace("<head>", "<head>\n" + seo_head_tags, 1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Favicon & Google Brand Schema injected successfully!")
