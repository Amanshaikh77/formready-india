import json
import os

DOCS_DIR = os.path.expanduser("~/formready-india/docs")
TOOLS_JSON = os.path.join(DOCS_DIR, "tools.json")

if not os.path.exists(TOOLS_JSON):
    print("tools.json not found!")
    exit(1)

with open(TOOLS_JSON, "r", encoding="utf-8") as f:
    tools = json.load(f)

for tool in tools:
    name = tool.get("name", "Online Tool")
    rel_path = tool.get("path", "")
    file_path = os.path.join(DOCS_DIR, rel_path)

    if not os.path.exists(file_path):
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already injected
    if "<!-- FORMREADY_SEO_START -->" in content:
        print(f"Skipping (Already optimized): {name}")
        continue

    seo_block = f"""
<!-- FORMREADY_SEO_START -->
<section style="max-width: 900px; margin: 40px auto 20px auto; padding: 24px; font-family: system-ui, -apple-system, sans-serif; line-height: 1.6; color: #a0907e; border-top: 1px solid rgba(217, 154, 63, 0.2);">
  <h2 style="color: #f5a623; font-size: 1.4rem; margin-bottom: 12px;">About {name}</h2>
  <p>Use our free <strong>{name}</strong> to process and prepare your documents or calculations instantly for sarkari jobs, online application forms, and official submissions. Fast, secure, and client-side processing.</p>

  <h3 style="color: #f8f4ec; font-size: 1.15rem; margin-top: 20px; margin-bottom: 8px;">How to use this tool:</h3>
  <ol style="padding-left: 20px;">
    <li>Enter the required details or upload your file.</li>
    <li>Adjust settings according to your application form guidelines.</li>
    <li>Click calculate, convert, or download to get instant results.</li>
  </ol>

  <h3 style="color: #f8f4ec; font-size: 1.15rem; margin-top: 20px; margin-bottom: 8px;">Frequently Asked Questions</h3>
  <p><strong>Is {name} free to use?</strong><br>Yes, this tool is 100% free with no hidden charges, sign-ups, or limits.</p>
  <p><strong>Is my data secure?</strong><br>Yes, processing happens directly inside your web browser. Your sensitive files and information are never stored on unauthorized servers.</p>
</section>
<!-- FORMREADY_SEO_END -->
"""

    if "</body>" in content:
        updated_content = content.replace("</body>", f"{seo_block}\n</body>")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"Successfully optimized: {name}")
    else:
        print(f"Warning: </body> not found in {file_path}")

print("\nAll tools SEO injection completed safely!")
