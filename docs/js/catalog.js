const TOOL_CATALOG = [
  {
    categoryId: "govt",
    categoryTitle: "🇮🇳 Indian Govt Form & ID Utilities",
    tools: [
      { slug: "aadhaar-pan-resizer", name: "Aadhaar / PAN Photo Resizer", icon: "🖼️", desc: "Exact 200x230 px & exact file size limit cropper/resizer", status: "active" },
      { slug: "aadhaar-pan-cutter", name: "Aadhaar / PAN Card Cutter", icon: "✂️", desc: "Crop and extract ID card sections cleanly for print", status: "active" },
      { slug: "signature-resizer", name: "Signature Resizer & Enhancer", icon: "✒️", desc: "Strict size limit with contrast boost for exam portal upload", status: "active" },
      { slug: "signature-maker", name: "Digital Signature Maker", icon: "✍️", desc: "Draw, smooth and download transparent digital signatures", status: "active" },
      { slug: "passport-photo-maker", name: "Passport Photo Maker", icon: "👥", desc: "Create ready-to-print passport size photo grids", status: "active" },
      { slug: "photo-sign-card", name: "Photo + Signature Joiner", icon: "🪪", desc: "Merge identity photo and signature into a single unified frame", status: "active" },
      { slug: "photo-sheet", name: "Passport Photo Sheet 4x6 / A4", icon: "🖨️", desc: "Generate printable photo sheets with cut borders", status: "active" },
      { slug: "document-scanner", name: "Document Scanner", icon: "📷", desc: "Camera scan with high-contrast B&W clean doc filter", status: "active" },
      { slug: "govt-pdf-helper", name: "Govt Form PDF Helper", icon: "📋", desc: "Compress & fit PDF strictly under required portal limits", status: "active" }
    ]
  },
  {
    categoryId: "pdf",
    categoryTitle: "📄 PDF Tools & Utilities",
    tools: [
      { slug: "pdf-editor", name: "PDF Editor", icon: "📝", desc: "Edit, annotate, and manage PDF documents directly in browser", status: "active" },
      { slug: "pdf-compressor", name: "Compress PDF", icon: "🗜️", desc: "Client-side file size compression keeping clarity intact", status: "active" },
      { slug: "merge-pdf", name: "Merge PDF", icon: "🔗", desc: "Combine multiple PDF documents into one indexed file", status: "active" },
      { slug: "split-pdf", name: "Split PDF", icon: "✂️", desc: "Extract pages or custom page ranges into a new PDF", status: "active" },
      { slug: "jpg-to-pdf", name: "JPG to PDF", icon: "🖼️", desc: "Convert photos and image files into multi-page PDFs", status: "active" },
      { slug: "pdf-to-jpg", name: "PDF to JPG", icon: "📸", desc: "Extract high-resolution JPG images from PDF pages", status: "active" },
      { slug: "rotate-pdf", name: "Rotate PDF", icon: "🔄", desc: "Fix orientation of 90°, 180°, or inverted pages", status: "active" },
      { slug: "pdf-organizer", name: "PDF Page Organizer", icon: "📑", desc: "Drag to reorder pages or delete unwanted sheets", status: "active" },
      { slug: "add-watermark", name: "Add Watermark", icon: "💧", desc: "Stamp confidential or custom text/logo over PDF pages", status: "active" }
    ]
  },
  {
    categoryId: "image",
    categoryTitle: "🖼️ Image & Photo Tools",
    tools: [
      { slug: "photo-resizer", name: "Photo Resizer", icon: "📐", desc: "Resize dimensions in pixels, cm, mm, and inches easily", status: "active" },
      { slug: "photo-compressor", name: "Photo Compressor", icon: "🗜️", desc: "Compress image file size strictly in KB without quality drop", status: "active" },
      { slug: "photo-cropper", name: "Photo Cropper", icon: "✂️", desc: "Crop photos with custom aspect ratios and preset dimensions", status: "active" },
      { slug: "image-converter", name: "Image Converter", icon: "🔄", desc: "Convert between JPG, PNG, WEBP, and other image formats", status: "active" },
      { slug: "background-remover", name: "Background Remover", icon: "🪄", desc: "Remove image background locally using client-side processing", status: "active" }
    ]
  },
  {
    categoryId: "text",
    categoryTitle: "🔤 Text & Generator Tools",
    tools: [
      { slug: "image-to-text", name: "Image to Text (OCR)", icon: "🔍", desc: "Extract text from photos and scanned documents offline", status: "active" },
      { slug: "text-cleaner", name: "Text Cleaner & Formatter", icon: "🧹", desc: "Remove duplicate spaces, line breaks, and messy formatting", status: "active" },
      { slug: "case-converter", name: "Case Converter", icon: "🔠", desc: "Convert text to UPPERCASE, lowercase, Title Case, etc.", status: "active" },
      { slug: "word-counter", name: "Word & Character Counter", icon: "📊", desc: "Real-time character, word, sentence, and reading time stats", status: "active" },
      { slug: "text-to-pdf", name: "Text to PDF", icon: "📄", desc: "Convert plain text notes into clean printable PDF documents", status: "active" },
      { slug: "lorem-generator", name: "Lorem Ipsum Generator", icon: "📜", desc: "Generate placeholder filler text for mockups and designs", status: "active" },
      { slug: "qr-generator", name: "QR Code Generator", icon: "📱", desc: "Create high-res QR codes for URLs, text, UPI, and WiFi", status: "active" },
      { slug: "barcode-generator", name: "Barcode Generator", icon: "🏷️", desc: "Generate Code128, EAN, and UPC barcodes instantly", status: "active" }
    ]
  },
  {
    categoryId: "calc",
    categoryTitle: "🧮 Everyday Calculators",
    tools: [
      { slug: "gst-calculator", name: "GST Calculator", icon: "💰", desc: "Inclusive and exclusive GST breakdown for Indian tax slabs", status: "active" },
      { slug: "age-calculator", name: "Age Calculator", icon: "🎂", desc: "Exact age in years, months, days, and form eligibility check", status: "active" },
      { slug: "emi-calculator", name: "EMI Calculator", icon: "💳", desc: "Calculate monthly installments and total loan interest", status: "active" },
      { slug: "discount-calculator", name: "Percentage & Discount", icon: "🏷️", desc: "Instant shopping discounts, markups, and margins", status: "active" },
      { slug: "bmi-calculator", name: "BMI & Health Calculator", icon: "⚖️", desc: "Body Mass Index calculation with health bracket indicators", status: "active" },
      { slug: "date-gap-calculator", name: "Date Gap Calculator", icon: "📅", desc: "Exact days, weeks, and month gaps between two dates", status: "active" },
      { slug: "unit-converter", name: "Unit Converter", icon: "📐", desc: "Convert Land, Weight, Length & Units", status: "active" },
      { slug: "currency-converter", name: "Currency Converter", icon: "💱", desc: "Quick currency rate estimations and conversions", status: "active" }
    ]
  }
];
