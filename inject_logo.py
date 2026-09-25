import re

file_path = "docs/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Futuristic Logo CSS
new_css = """
    /* --- ULTRA FUTURISTIC HERO LOGO --- */
    .hero-brand-box {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px 10px 14px;
      text-align: center;
    }
    .hero-logo-row {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      margin-bottom: 8px;
    }
    .futuristic-shield-icon {
      width: 52px;
      height: 52px;
      background: radial-gradient(circle at 35% 35%, rgba(255, 184, 77, 0.4), rgba(245, 166, 35, 0.08) 75%);
      border: 2px solid rgba(245, 166, 35, 0.7);
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      box-shadow: 0 0 24px rgba(245, 166, 35, 0.45), inset 0 0 14px rgba(245, 166, 35, 0.25);
      animation: cyberPulse 2.8s ease-in-out infinite alternate;
      flex-shrink: 0;
    }
    @keyframes cyberPulse {
      0% {
        transform: translateY(0px) scale(1);
        box-shadow: 0 0 16px rgba(245, 166, 35, 0.35), inset 0 0 10px rgba(245, 166, 35, 0.2);
        border-color: rgba(245, 166, 35, 0.6);
      }
      100% {
        transform: translateY(-3px) scale(1.06);
        box-shadow: 0 0 32px rgba(245, 166, 35, 0.75), inset 0 0 20px rgba(245, 166, 35, 0.45);
        border-color: #ffb84d;
      }
    }
    .hero-title-text {
      font-family: 'Space Grotesk', sans-serif !important;
      font-size: clamp(28px, 6.5vw, 42px) !important;
      font-weight: 800 !important;
      letter-spacing: -0.5px;
      line-height: 1.1;
      display: flex;
      align-items: center;
      gap: 8px;
      user-select: none;
      margin: 0 !important;
    }
    .brand-white {
      background: linear-gradient(180deg, #FFFFFF 25%, #d1cfc7 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 2px 10px rgba(255, 255, 255, 0.3));
    }
    .brand-amber {
      background: linear-gradient(135deg, #ffc875 0%, #f5a623 55%, #d97706 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 0 18px rgba(245, 166, 35, 0.7));
    }
    .hero-subtitle {
      font-size: clamp(12px, 3.2vw, 14px) !important;
      color: #a0907e !important;
      font-weight: 500 !important;
      margin: 6px 0 10px !important;
      letter-spacing: 0.3px;
    }
    .creator-glow-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11.5px;
      font-weight: 700;
      color: #ffc875;
      background: rgba(245, 166, 35, 0.1);
      border: 1px solid rgba(245, 166, 35, 0.35);
      padding: 4px 14px;
      border-radius: 999px;
      letter-spacing: 0.4px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.6);
    }
"""

if ".hero-brand-box" not in html:
    html = html.replace("</style>", new_css + "\n</style>", 1)

# 2. Modern Futuristic HTML Structure
new_markup = """
    <div class="hero-brand-box">
      <div class="hero-logo-row">
        <div class="futuristic-shield-icon">⚡</div>
        <h1 class="hero-title-text">
          <span class="brand-white">FormReady</span>
          <span class="brand-amber">India</span>
        </h1>
      </div>
      <p class="hero-subtitle">Superfast 100% Secure Offline-Capable Document & Form Toolbox</p>
      <div class="creator-glow-pill">✨ Made by Aman Shaikh</div>
    </div>
"""

# Replace anything matching the old logo structure (lightning + FormReady India)
pattern = r'<div[^>]*class=["\'][^"\']*header[^"\']*["\'][^>]*>[\s\S]*?FormReady\s+India[\s\S]*?Aman\s+Shaikh[\s\S]*?<\/div>\s*<\/div>'
replaced_html = re.sub(pattern, new_markup.strip(), html)

if replaced_html == html:
    # Alternative direct regex for common variations
    alt_pattern = r'(\s*<[^>]+>\s*⚡\s*FormReady\s+India[\s\S]*?Aman\s+Shaikh[\s\S]*?<\/[^>]+>)'
    replaced_html = re.sub(alt_pattern, new_markup, html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(replaced_html)

print("Updated docs/index.html successfully!")
