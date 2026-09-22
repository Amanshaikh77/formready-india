const TOOL_CATALOG = [
  {
    categoryId: "govt",
    categoryTitle: "🇮🇳 Indian Govt Form & ID Utilities",
    tools: [
      { slug: "aadhaar-pan-resizer", name: "Aadhaar / PAN Photo Resizer", icon: "🖼️", desc: "Exact 200x230 px & exact file size limit cropper/resizer", status: "active" },
      { slug: "signature-resizer", name: "Signature Resizer & Enhancer", icon: "✒️", desc: "Strict size limit with contrast boost for exam portal upload", status: "active" },
      { slug: "passport-photo-maker", name: "Passport Photo + Sign Card", icon: "👥", desc: "Merge identity photo and signature into a single unified frame", status: "active" },
      { slug: "document-scanner", name: "Document Scanner", icon: "📷", desc: "Camera scan with high-contrast B&W clean doc filter", status: "active" },
      { slug: "govt-pdf-helper", name: "Govt Form PDF Helper", icon: "📋", desc: "Compress & fit PDF strictly under required portal limits", status: "active" }
    ]
  },
  {
    categoryId: "pdf",
    categoryTitle: "📄 PDF Tools & Editors",
    tools: [
      { slug: "pdf-text-inspector", name: "PDF Text Inspector & Editor", icon: "📄", desc: "Inspect text, redactions, and forms in PDFs securely", status: "active" },
      { slug: "merge-pdf", name: "Merge PDF", icon: "🔗", desc: "Combine multiple PDF documents into one indexed file", status: "active" },
      { slug: "split-pdf", name: "Split PDF", icon: "✂️", desc: "Extract pages or custom page ranges into a new PDF", status: "active" },
      { slug: "jpg-to-pdf", name: "JPG to PDF", icon: "🖼️", desc: "Convert photos and image files into multi-page PDFs", status: "active" },
      { slug: "pdf-to-jpg", name: "PDF to JPG", icon: "📸", desc: "Extract high-resolution JPG images from PDF pages", status: "active" },
      { slug: "pdf-compressor", name: "Compress PDF", icon: "🗜️", desc: "Client-side file size compression keeping clarity intact", status: "active" },
      { slug: "rotate-pdf", name: "Rotate PDF", icon: "🔄", desc: "Fix orientation of 90°, 180°, or inverted pages", status: "active" },
      { slug: "pdf-organizer", name: "PDF Page Organizer", icon: "📑", desc: "Drag to reorder pages or delete unwanted sheets", status: "active" },
      { slug: "add-watermark", name: "Add Watermark", icon: "💧", desc: "Stamp confidential or custom text/logo over PDF pages", status: "active" }
    ]
  },
  {
    categoryId: "text",
    categoryTitle: "📝 Text, Code & Content Tools",
    tools: [
      { slug: "word-counter", name: "Word & Character Counter", icon: "📊", desc: "Real-time count of words, characters, and reading time", status: "active" },
      { slug: "case-converter", name: "Case Converter", icon: "🔤", desc: "Toggle UPPERCASE, lower case, Title Case & camelCase", status: "active" },
      { slug: "text-cleaner", name: "Text Cleaner", icon: "🧹", desc: "Strip accidental double spaces, tabs, and blank lines", status: "active" },
      { slug: "qr-generator", name: "QR Code Generator", icon: "🏁", desc: "Create QR codes for links, UPI payments, and Wi-Fi", status: "active" },
      { slug: "barcode-generator", name: "Barcode Generator", icon: "📶", desc: "Generate standard barcodes easily", status: "active" },
      { slug: "text-to-pdf", name: "Text to PDF / Image", icon: "📜", desc: "Convert plain text notes into a printable document", status: "active" },
      { slug: "lorem-generator", name: "Lorem Ipsum Generator", icon: "📜", desc: "Generate placeholder text for layouts and forms", status: "active" }
    ]
  },
  {
    categoryId: "calc",
    categoryTitle: "🧮 Daily & Finance Calculators",
    tools: [
      { slug: "age-calculator", name: "Govt Form Age Calculator", icon: "🎂", desc: "Calculate exact age as on notification date (Y/M/D)", status: "active" },
      { slug: "gst-calculator", name: "GST Calculator", icon: "🧾", desc: "Breakdown CGST, SGST & total amount (add/remove)", status: "active" },
      { slug: "emi-calculator", name: "EMI Calculator", icon: "💳", desc: "Calculate monthly installments and total loan interest", status: "active" },
      { slug: "discount-calculator", name: "Percentage & Discount", icon: "🏷️", desc: "Instant shopping discounts, markups, and margins", status: "active" },
      { slug: "bmi-calculator", name: "BMI & Health Calculator", icon: "⚖️", desc: "Body Mass Index calculation with health bracket indicators", status: "active" },
      { slug: "date-gap-calculator", name: "Date Gap Calculator", icon: "📅", desc: "Exact days, weeks, and month gaps between two dates", status: "active" },
      { slug: "unit-converter", name: "Unit Converter", icon: "📐", desc: "Convert Land, Weight, Length & Units", status: "active" },
      { slug: "currency-converter", name: "Currency Converter", icon: "💱", desc: "Quick currency rate estimations and conversions", status: "active" }
    ]
  }

];
