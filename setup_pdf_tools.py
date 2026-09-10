import os, re

base_css = """
:root {
  --bg: #151210;
  --panel: #1e1a17;
  --line: #39322b;
  --amber: #d99a3f;
  --paper: #f2ece2;
  --muted: #a89a89;
  --card-bg: #14110f;
  --danger: #ef4444;
  --success: #22c55e;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: var(--bg);
  color: var(--paper);
  font-family: 'Inter', sans-serif;
  margin: 0;
  padding: 14px;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  touch-action: pan-y;
}
.wrapper { width: 100%; max-width: 540px; }
@media (min-width: 768px) { .wrapper { max-width: 740px; } }
.back-link {
  color: var(--amber);
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  display: inline-block;
  margin-bottom: 12px;
}
.card {
  background: var(--panel);
  border: 1px solid var(--line);
  padding: 18px;
  border-radius: 12px;
  width: 100%;
  margin-bottom: 14px;
}
h2 { color: var(--amber); margin-bottom: 4px; font-size: 20px; text-align: center; }
.subtitle { color: var(--muted); font-size: 12px; margin-bottom: 16px; text-align: center; }
.upload-box {
  border: 2px dashed var(--amber);
  background: rgba(217, 154, 63, 0.05);
  border-radius: 10px;
  padding: 22px 14px;
  text-align: center;
  cursor: pointer;
  margin-bottom: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}
.upload-box span { color: var(--amber); font-weight: 600; font-size: 14px; }
.upload-box small { color: var(--muted); font-size: 11px; }
.item-list { display: flex; flex-direction: column; gap: 8px; margin-bottom: 16px; }
.item-row {
  background: var(--card-bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
}
.item-name { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 65%; }
.row-actions { display: flex; gap: 6px; }
.mini-btn {
  background: #2a2420;
  color: var(--paper);
  border: 1px solid var(--line);
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 11px;
  cursor: pointer;
}
.mini-btn:hover { background: var(--amber); color: var(--bg); }
.mini-btn.del:hover { background: var(--danger); color: #fff; }
.btn {
  background: var(--amber);
  color: var(--bg);
  border: none;
  padding: 12px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  text-align: center;
  width: 100%;
}
.btn:hover { opacity: 0.9; }
.input-text {
  width: 100%;
  background: var(--card-bg);
  border: 1px solid var(--line);
  color: var(--paper);
  padding: 10px 12px;
  border-radius: 8px;
  font-size: 13px;
  margin-bottom: 14px;
  outline: none;
}
.input-text:focus { border-color: var(--amber); }
.grid-thumbs {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
  gap: 12px;
  margin-top: 16px;
}
.thumb-card {
  background: var(--card-bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}
.thumb-card img { width: 100%; height: 160px; object-fit: contain; background: #000; border-radius: 4px; }
"""

# 1. MERGE PDF
merge_pdf_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Merge PDF - FormReady India</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
<style>{base_css}</style>
</head>
<body>
<div class="wrapper">
  <a href="../../index.html" class="back-link">&larr; Back to Dashboard</a>
  <div class="card">
    <h2>Merge PDF</h2>
    <div class="subtitle">Combine multiple PDF documents into one single file</div>
    <input type="file" id="pdf-input" accept="application/pdf" multiple style="display:none">
    <div class="upload-box" onclick="document.getElementById('pdf-input').click()">
      <span>📑 Tap to Select PDF Files</span>
      <small>Select 2 or more PDF files</small>
    </div>
    <div class="item-list" id="pdf-list"></div>
    <button class="btn" id="merge-btn" style="display:none">⚡ Merge and Download PDF</button>
  </div>
</div>
<script>
  let pdfs = [];
  const input = document.getElementById('pdf-input');
  const listEl = document.getElementById('pdf-list');
  const mergeBtn = document.getElementById('merge-btn');

  input.addEventListener('change', async (e) => {
    for (const file of e.target.files) {
      const buffer = await file.arrayBuffer();
      pdfs.push({ name: file.name, buffer });
    }
    input.value = '';
    render();
  });

  function render() {
    listEl.innerHTML = '';
    pdfs.forEach((p, idx) => {
      const row = document.createElement('div');
      row.className = 'item-row';
      row.innerHTML = `
        <span class="item-name">${idx + 1}. ${p.name}</span>
        <div class="row-actions">
          <button class="mini-btn" onclick="shift(${idx}, -1)" ${idx === 0 ? 'disabled' : ''}>▲</button>
          <button class="mini-btn" onclick="shift(${idx}, 1)" ${idx === pdfs.length - 1 ? 'disabled' : ''}>▼</button>
          <button class="mini-btn del" onclick="removePdf(${idx})">✕</button>
        </div>
      `;
      listEl.appendChild(row);
    });
    mergeBtn.style.display = pdfs.length >= 2 ? 'block' : 'none';
  }

  window.shift = (idx, dir) => {
    const target = idx + dir;
    if (target < 0 || target >= pdfs.length) return;
    const temp = pdfs[idx];
    pdfs[idx] = pdfs[target];
    pdfs[target] = temp;
    render();
  };

  window.removePdf = (idx) => {
    pdfs.splice(idx, 1);
    render();
  };

  mergeBtn.addEventListener('click', async () => {
    mergeBtn.textContent = 'Merging...';
    mergeBtn.disabled = true;
    try {
      const mergedPdf = await PDFLib.PDFDocument.create();
      for (const p of pdfs) {
        const doc = await PDFLib.PDFDocument.load(p.buffer);
        const copiedPages = await mergedPdf.copyPages(doc, doc.getPageIndices());
        copiedPages.forEach((page) => mergedPdf.addPage(page));
      }
      const mergedBytes = await mergedPdf.save();
      const blob = new Blob([mergedBytes], { type: 'application/pdf' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'merged_document.pdf';
      link.click();
    } catch (err) {
      alert('Error merging PDFs: ' + err.message);
    }
    mergeBtn.textContent = '⚡ Merge and Download PDF';
    mergeBtn.disabled = false;
  });
</script>
</body>
</html>"""

# 2. SPLIT PDF
split_pdf_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Split PDF - FormReady India</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
<style>{base_css}</style>
</head>
<body>
<div class="wrapper">
  <a href="../../index.html" class="back-link">&larr; Back to Dashboard</a>
  <div class="card">
    <h2>Split PDF</h2>
    <div class="subtitle">Extract specific page numbers or ranges into a separate PDF</div>
    <input type="file" id="split-input" accept="application/pdf" style="display:none">
    <div class="upload-box" id="upload-zone" onclick="document.getElementById('split-input').click()">
      <span>📑 Tap to Select PDF File</span>
      <small>Single PDF to extract pages from</small>
    </div>

    <div id="split-controls" style="display:none">
      <div id="file-info" style="font-size:13px; color:var(--amber); margin-bottom:12px; text-align:center;"></div>
      <label style="font-size:12px; color:var(--muted); display:block; margin-bottom:6px;">
        Page Range to Extract (e.g. 1-3, 5, 8-10):
      </label>
      <input type="text" id="range-input" class="input-text" placeholder="e.g. 1-2, 4">
      <button class="btn" id="extract-btn">✂️ Extract Pages & Download</button>
    </div>
  </div>
</div>
<script>
  let pdfBytes = null;
  let totalPages = 0;
  const input = document.getElementById('split-input');
  const controls = document.getElementById('split-controls');
  const fileInfo = document.getElementById('file-info');
  const rangeInput = document.getElementById('range-input');
  const extractBtn = document.getElementById('extract-btn');

  input.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    pdfBytes = await file.arrayBuffer();
    const pdfDoc = await PDFLib.PDFDocument.load(pdfBytes);
    totalPages = pdfDoc.getPageCount();
    fileInfo.textContent = `${file.name} (Total Pages: ${totalPages})`;
    rangeInput.value = `1-${Math.min(totalPages, 2)}`;
    controls.style.display = 'block';
  });

  extractBtn.addEventListener('click', async () => {
    const raw = rangeInput.value.trim();
    if (!raw) return alert('Please enter page numbers or range.');

    const pagesToExtract = new Set();
    const parts = raw.split(',');
    for (const part of parts) {
      const match = part.trim().match(/^(\d+)(?:-(\d+))?$/);
      if (match) {
        const start = parseInt(match[1], 10);
        const end = match[2] ? parseInt(match[2], 10) : start;
        for (let i = start; i <= end; i++) {
          if (i >= 1 && i <= totalPages) pagesToExtract.add(i - 1);
        }
      }
    }

    if (pagesToExtract.size === 0) return alert('Invalid range or pages out of bounds.');

    extractBtn.textContent = 'Extracting...';
    extractBtn.disabled = true;

    try {
      const srcDoc = await PDFLib.PDFDocument.load(pdfBytes);
      const newDoc = await PDFLib.PDFDocument.create();
      const pageIndices = Array.from(pagesToExtract).sort((a, b) => a - b);
      const copied = await newDoc.copyPages(srcDoc, pageIndices);
      copied.forEach((p) => newDoc.addPage(p));

      const outBytes = await newDoc.save();
      const blob = new Blob([outBytes], { type: 'application/pdf' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = `extracted_pages.pdf`;
      link.click();
    } catch (err) {
      alert('Error extracting: ' + err.message);
    }
    extractBtn.textContent = '✂️ Extract Pages & Download';
    extractBtn.disabled = false;
  });
</script>
</body>
</html>"""

# 3. JPG TO PDF
jpg_to_pdf_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>JPG to PDF - FormReady India</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
<style>{base_css}</style>
</head>
<body>
<div class="wrapper">
  <a href="../../index.html" class="back-link">&larr; Back to Dashboard</a>
  <div class="card">
    <h2>JPG to PDF Converter</h2>
    <div class="subtitle">Convert images (JPG, PNG) into a single high-quality PDF</div>
    <input type="file" id="img-input" accept="image/*" multiple style="display:none">
    <div class="upload-box" onclick="document.getElementById('img-input').click()">
      <span>🖼️ Tap to Select Images</span>
      <small>JPG or PNG files</small>
    </div>
    <div class="item-list" id="img-list"></div>
    <button class="btn" id="conv-btn" style="display:none">📄 Convert to PDF & Download</button>
  </div>
</div>
<script>
  let images = [];
  const input = document.getElementById('img-input');
  const listEl = document.getElementById('img-list');
  const convBtn = document.getElementById('conv-btn');

  input.addEventListener('change', async (e) => {
    for (const file of e.target.files) {
      const buffer = await file.arrayBuffer();
      images.push({ name: file.name, type: file.type, buffer });
    }
    input.value = '';
    render();
  });

  function render() {
    listEl.innerHTML = '';
    images.forEach((img, idx) => {
      const row = document.createElement('div');
      row.className = 'item-row';
      row.innerHTML = `
        <span class="item-name">${idx + 1}. ${img.name}</span>
        <div class="row-actions">
          <button class="mini-btn" onclick="shiftImg(${idx}, -1)" ${idx === 0 ? 'disabled' : ''}>▲</button>
          <button class="mini-btn" onclick="shiftImg(${idx}, 1)" ${idx === images.length - 1 ? 'disabled' : ''}>▼</button>
          <button class="mini-btn del" onclick="removeImg(${idx})">✕</button>
        </div>
      `;
      listEl.appendChild(row);
    });
    convBtn.style.display = images.length > 0 ? 'block' : 'none';
  }

  window.shiftImg = (idx, dir) => {
    const target = idx + dir;
    if (target < 0 || target >= images.length) return;
    const temp = images[idx];
    images[idx] = images[target];
    images[target] = temp;
    render();
  };

  window.removeImg = (idx) => {
    images.splice(idx, 1);
    render();
  };

  convBtn.addEventListener('click', async () => {
    convBtn.textContent = 'Generating PDF...';
    convBtn.disabled = true;
    try {
      const pdfDoc = await PDFLib.PDFDocument.create();
      for (const img of images) {
        let embedded;
        if (img.type === 'image/png') {
          embedded = await pdfDoc.embedPng(img.buffer);
        } else {
          embedded = await pdfDoc.embedJpg(img.buffer);
        }
        const page = pdfDoc.addPage([embedded.width, embedded.height]);
        page.drawImage(embedded, { x: 0, y: 0, width: embedded.width, height: embedded.height });
      }
      const pdfBytes = await pdfDoc.save();
      const blob = new Blob([pdfBytes], { type: 'application/pdf' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'converted_images.pdf';
      link.click();
    } catch (err) {
      alert('Error creating PDF: ' + err.message);
    }
    convBtn.textContent = '📄 Convert to PDF & Download';
    convBtn.disabled = false;
  });
</script>
</body>
</html>"""

# 4. PDF TO JPG
pdf_to_jpg_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>PDF to JPG - FormReady India</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
<style>{base_css}</style>
</head>
<body>
<div class="wrapper">
  <a href="../../index.html" class="back-link">&larr; Back to Dashboard</a>
  <div class="card">
    <h2>PDF to JPG Extractor</h2>
    <div class="subtitle">Extract all PDF pages as high-resolution JPG images</div>
    <input type="file" id="pdf-to-img-input" accept="application/pdf" style="display:none">
    <div class="upload-box" onclick="document.getElementById('pdf-to-img-input').click()">
      <span>📸 Tap to Select PDF</span>
      <small>Render pages to JPG format</small>
    </div>
    <div id="status-text" style="font-size:12px; color:var(--amber); text-align:center; margin-bottom:10px;"></div>
    <div class="grid-thumbs" id="thumb-grid"></div>
  </div>
</div>
<script>
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
  const input = document.getElementById('pdf-to-img-input');
  const grid = document.getElementById('thumb-grid');
  const status = document.getElementById('status-text');

  input.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    grid.innerHTML = '';
    status.textContent = 'Loading and extracting pages...';

    const buffer = await file.arrayBuffer();
    const pdf = await pdfjsLib.getDocument({ data: buffer }).promise;
    status.textContent = `Found ${pdf.numPages} pages. Rendering...`;

    for (let i = 1; i <= pdf.numPages; i++) {
      const page = await pdf.getPage(i);
      const viewport = page.getViewport({ scale: 1.5 });
      const canvas = document.createElement('canvas');
      canvas.width = viewport.width;
      canvas.height = viewport.height;
      const ctx = canvas.getContext('2d');
      await page.render({ canvasContext: ctx, viewport }).promise;

      const imgUrl = canvas.toDataURL('image/jpeg', 0.92);
      const card = document.createElement('div');
      card.className = 'thumb-card';
      card.innerHTML = `
        <img src="${imgUrl}" alt="Page ${i}">
        <span style="font-size:11px;">Page ${i}</span>
        <a href="${imgUrl}" download="page_${i}.jpg" class="mini-btn" style="text-decoration:none;">Download JPG</a>
      `;
      grid.appendChild(card);
    }
    status.textContent = `Completed extraction for ${pdf.numPages} pages.`;
  });
</script>
</body>
</html>"""

tools_map = {
    "merge-pdf": merge_pdf_code,
    "split-pdf": split_pdf_code,
    "jpg-to-pdf": jpg_to_pdf_code,
    "pdf-to-jpg": pdf_to_jpg_code
}

for tool_slug, content in tools_map.items():
    paths = [
        f"tools/{tool_slug}/index.html",
        f"tools/{tool_slug}.html",
        f"docs/tools/{tool_slug}/index.html",
        f"docs/tools/{tool_slug}.html"
    ]
    for p in paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created: {p}")

# Ensure exact relative link on Dashboard
for idx in ["index.html", "docs/index.html"]:
    if not os.path.exists(idx):
        continue
    with open(idx, "r", encoding="utf-8") as f:
        html = f.read()

    html = re.sub(r'href=["\'](?:/|docs/)?tools/merge-pdf(?:\.html|/index\.html)?["\']', 'href="tools/merge-pdf/index.html"', html)
    html = re.sub(r'href=["\'](?:/|docs/)?tools/split-pdf(?:\.html|/index\.html)?["\']', 'href="tools/split-pdf/index.html"', html)
    html = re.sub(r'href=["\'](?:/|docs/)?tools/jpg-to-pdf(?:\.html|/index\.html)?["\']', 'href="tools/jpg-to-pdf/index.html"', html)
    html = re.sub(r'href=["\'](?:/|docs/)?tools/pdf-to-jpg(?:\.html|/index\.html)?["\']', 'href="tools/pdf-to-jpg/index.html"', html)

    with open(idx, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated links in: {idx}")

print("\nSUCCESS: All 4 PDF tools are fully active and connected!")
