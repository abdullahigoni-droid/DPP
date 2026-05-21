# Digital Product Passport (DPP) Generator

A Python-based system for generating self-contained HTML Digital Product Passports for remanufactured turbochargers. The generated HTML files are fully offline-capable with all data, styles, and interactivity embedded inline.

## 🎯 Features

- **Self-contained HTML**: Single file with embedded CSS, JavaScript, and data
- **QR Code Generation**: High error-correction QR codes for laser-etched durability
- **Made2Verify-style DPP IDs**: `dpp_` prefixed identifiers with stable route output
- **Dashboard Interface**: Product overview, environmental impact, materials, journey, remanufacturing, testing, lifecycle, support, and raw JSON
- **Embedded Product Image**: Uses the local turbocharger image so generated passports stay portable
- **Responsive Design**: Works on desktop and mobile devices
- **Offline Capable**: No internet connection required after generation
- **Print-ready Labels**: Separate QR code PNG for physical labeling

## 📁 Project Structure

```
dpp_mvp/
├── generate_dpp.py          # Main generator script
├── data/
│   └── sample_turbo_dpp.py  # Sample DPP data
├── templates/
│   └── dpp_template.html    # Jinja2 HTML template
├── output/                  # Generated files (gitignored)
│   ├── dpp_TTG-TRB-2026-00147.html
│   └── label_TTG-TRB-2026-00147.png
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download** this repository

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate a DPP**:
   ```bash
   python generate_dpp.py
   ```

4. **View the output**:
   - Open `output/dpp_*.html` in any web browser
   - Print `output/label_*.png` for physical labeling

## 📊 Data Structure

The DPP data is defined in `data/sample_turbo_dpp.py` and currently models a remanufactured turbocharger for The Turbo Guy. It includes:

### Product Overview
- Original core information (OEM part, serial number, vehicle fitment)
- Remanufacturer details (company, facility, EOID)
- Remanufactured unit tracking

### Remanufacturing Operations
- Component disposition (Reused, Reconditioned, Replaced, Upgraded)
- Testing & calibration records (VSR balancing, actuator calibration, leak test)

### Sustainability & Materials
- Global Warming Potential (GWP) comparison
- Material circularity percentage
- Energy consumption data
- Material composition and traceability

### Lifecycle & Support
- Warranty and returns guidance
- Installation guidance with torque specifications
- End-of-life takeback scheme
- The Turbo Guy trade support details

## 🔧 Customization

### Modifying Data

Edit `data/sample_turbo_dpp.py` to change:
- Company information
- Technical specifications
- Sustainability metrics
- Warranty terms

### Changing the Passport URL or ID

The default URL pattern is:
```
https://yourcompany.github.io/DPP/{dpp_id}/
```

To change this, modify the `passport_url` and `dpp_id` fields in `sample_turbo_dpp.py`. To force a fresh ID at generation time, set `DPP_GENERATE_NEW=1`; to override with a specific ID, set `DPP_ID`.

### Template Styling

The HTML template is in `templates/dpp_template.html`. Key customization points:

- **Colors**: Edit CSS variables in the `:root` selector
- **Layout**: Modify CSS grid/flexbox rules
- **Content**: Change Jinja2 template blocks

## 🏗️ Deployment

### GitHub Pages (Recommended)

1. Create or connect the GitHub repository
2. Push the `main` branch to GitHub
3. In repository settings, set Pages source to **Deploy from a branch**
4. Select the `main` branch and `/docs` folder

For this repository, the live site URL will be:
```
https://abdullahigoni-droid.github.io/DPP/
```

Commit `docs/index.html` for the live homepage. The generator also creates a `/{DPP_ID}/` route so the embedded QR code links directly to the deployed passport.

### Netlify / Vercel

1. Drag and drop the `output/` folder
2. Each HTML file will be accessible via its own URL
3. Update the passport URL pattern in the generator

### Self-hosting

Upload the HTML files to any web server. No backend required!

## 🔄 Batch Generation

To generate multiple passports, modify `generate_dpp.py`:

```python
from data.sample_turbo_dpp import DPP_DATA

# List of variations
units = [
    {"tracking_id": "TTG-TRB-2026-00147", "serial": "TTG-VNT-2026-00147"},
    {"tracking_id": "TTG-TRB-2026-00148", "serial": "TTG-VNT-2026-00148"},
    # ... more units
]

for unit in units:
    data = DPP_DATA.copy()
    data["remanufactured_unit"]["tracking_id"] = unit["tracking_id"]
    data["original_core"]["serial_number"] = unit["serial"]
    # ... generate DPP for this unit
```

## 🛠️ Technical Details

### Dependencies

- **Jinja2**: HTML templating
- **qrcode[pil]**: QR code generation with PIL support
- **Pillow**: Image processing (required by qrcode)
- **python-ulid**: Optional fresh ID generation when `DPP_GENERATE_NEW=1`

### QR Code Specifications

- **Error Correction**: H (30% recovery capacity)
- **Box Size**: 10 pixels
- **Border**: 4 modules
- **Format**: PNG, 490×490 pixels

### DPP ID Format

DPP IDs use a `dpp_` prefix followed by a stable identifier:
```
dpp_01KTTG4PV63D5D8JB7M2VNT001
```

Set `DPP_GENERATE_NEW=1` to generate a fresh ULID-backed identifier at runtime.

## 📄 Compliance

This DPP generator aligns with:

- **EU Ecodesign for Sustainable Products Regulation (ESPR)**
- **EU 2023/1542** — Remanufactured goods warranty parity
- **ISO 14044** — Life Cycle Assessment methodology
- **ISO 21940-11** — Residual unbalance testing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with `python generate_dpp.py`
5. Submit a pull request

## 📝 License

MIT License — feel free to use and modify for your projects.

## 🆘 Support

For issues or questions:

1. Check the project issue tracker
2. Review the template file for customization options
3. Verify Python version and dependencies

## 🔄 Future Enhancements

- [ ] API integration for ERP/MES data pull
- [ ] Multi-language support
- [ ] PDF export option
- [ ] Digital signature verification
- [ ] Blockchain anchoring for authenticity
- [ ] Mobile app for QR scanning

---

**Built with ❤️ for the circular economy**
