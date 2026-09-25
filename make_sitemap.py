import json
import os
from datetime import date

DOCS_DIR = os.path.expanduser("~/formready-india/docs")
TOOLS_JSON = os.path.join(DOCS_DIR, "tools.json")
SITEMAP_PATH = os.path.join(DOCS_DIR, "sitemap.xml")

BASE_URL = "https://formready-india.onrender.com"
today = date.today().isoformat()

with open(TOOLS_JSON, "r", encoding="utf-8") as f:
    tools = json.load(f)

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    '  <url>',
    f'    <loc>{BASE_URL}/</loc>',
    f'    <lastmod>{today}</lastmod>',
    '    <priority>1.00</priority>',
    '  </url>'
]

for tool in tools:
    path = tool.get("path", "").replace("index.html", "")
    full_url = f"{BASE_URL}/{path}"
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{full_url}</loc>')
    xml_lines.append(f'    <lastmod>{today}</lastmod>')
    xml_lines.append('    <priority>0.80</priority>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')

with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(xml_lines))

print("sitemap.xml with Render URL created successfully!")
