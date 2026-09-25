import re

file_path = "docs/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. CSS for 2D/3D Toggle Switch and 3D Perspective Transformation
css_3d = """
    /* --- 2D / 3D CYBER TOGGLE SWITCH --- */
    .top-mode-bar {
      position: absolute;
      top: 16px;
      left: 16px;
      z-index: 1000;
    }
    .toggle-3d-wrap {
      display: inline-flex;
      align-items: center;
      background: rgba(20, 16, 12, 0.85);
      border: 1px solid rgba(245, 166, 35, 0.35);
      border-radius: 999px;
      padding: 3px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5), inset 0 0 10px rgba(245, 166, 35, 0.1);
      backdrop-filter: blur(8px);
    }
    .toggle-btn {
      border: none;
      background: transparent;
      color: #a0907e;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 11.5px;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .toggle-btn.active {
      background: linear-gradient(135deg, #f5a623, #d97706);
      color: #0c0a08;
      box-shadow: 0 0 12px rgba(245, 166, 35, 0.6);
    }

    /* --- 3D PERSPECTIVE ENVIRONMENT WHEN 3D IS ON --- */
    body.mode-3d-active {
      perspective: 1400px;
      perspective-origin: center 250px;
    }
    body.mode-3d-active .tool-card,
    body.mode-3d-active [class*="card"],
    body.mode-3d-active .category-section {
      transform-style: preserve-3d;
      transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.4s ease;
    }
    body.mode-3d-active .tool-card {
      transform: translateZ(20px) rotateX(4deg);
      box-shadow: 0 16px 32px rgba(0,0,0,0.7), 0 0 15px rgba(245, 166, 35, 0.15) !important;
      border-color: rgba(245, 166, 35, 0.4) !important;
    }
    body.mode-3d-active .tool-card:hover {
      transform: translateZ(45px) rotateX(0deg) scale(1.03);
      box-shadow: 0 24px 45px rgba(0,0,0,0.85), 0 0 25px rgba(245, 166, 35, 0.4) !important;
      border-color: #f5a623 !important;
    }
    body.mode-3d-active .futuristic-shield-icon {
      transform: translateZ(30px) rotateY(-10deg);
      box-shadow: -8px 8px 30px rgba(245, 166, 35, 0.6) !important;
    }

    /* Support for Custom 3D Section Visibility */
    #section-3d {
      display: none;
      animation: fadeIn3D 0.5s ease;
    }
    body.mode-3d-active #section-3d {
      display: block;
    }
    body.mode-3d-active #section-2d-default {
      display: none;
    }
    @keyframes fadeIn3D {
      from { opacity: 0; transform: translateY(20px) scale(0.97); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }
"""

if ".toggle-3d-wrap" not in html:
    html = html.replace("</style>", css_3d + "\n</style>", 1)

# 2. Add Toggle Button in HTML Header Area
toggle_html = """
    <!-- 2D / 3D Mode Switcher -->
    <div class="top-mode-bar">
      <div class="toggle-3d-wrap">
        <button type="button" class="toggle-btn active" id="btnMode2D" onclick="setDimensionMode('2d')">2D</button>
        <button type="button" class="toggle-btn" id="btnMode3D" onclick="setDimensionMode('3d')">⚡ 3D</button>
      </div>
    </div>
"""

# Insert right after body tag opens
if "top-mode-bar" not in html:
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + toggle_html, html, 1)

# 3. JavaScript Logic for 2D/3D Switching and LocalStorage persistence
script_3d = """
<script>
function setDimensionMode(mode) {
  const is3D = (mode === '3d');
  document.body.classList.toggle('mode-3d-active', is3D);
  
  const b2d = document.getElementById('btnMode2D');
  const b3d = document.getElementById('btnMode3D');
  if (b2d && b3d) {
    b2d.classList.toggle('active', !is3D);
    b3d.classList.toggle('active', is3D);
  }

  // Toggle user's custom 3D element if present
  const sec3d = document.getElementById('section-3d');
  const sec2d = document.getElementById('section-2d-default');
  if (sec3d && sec2d) {
    sec3d.style.display = is3D ? 'block' : 'none';
    sec2d.style.display = is3D ? 'none' : 'block';
  }

  localStorage.setItem('formready_dim_mode', mode);
}

// Restore saved preference on load
window.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('formready_dim_mode') || '2d';
  setDimensionMode(saved);
});
</script>
"""

if "setDimensionMode" not in html:
    html = html.replace("</body>", script_3d + "\n</body>", 1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("2D/3D Mode Switcher injected into docs/index.html successfully!")
