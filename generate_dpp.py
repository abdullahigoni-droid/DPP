#!/usr/bin/env python3
"""
Digital Product Passport (DPP) Generator for Remanufactured Turbochargers

This script generates a self-contained HTML file representing a Digital Product Passport.
The HTML file is fully offline-capable with all data, styles, and interactivity inline.

Usage:
    python generate_dpp.py
"""

import base64
import mimetypes
import io
import json
import os
import sys
from pathlib import Path

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_H
except ImportError:
    print("❌ Error: qrcode library not installed.")
    print("   Run: pip install qrcode[pil]")
    sys.exit(1)

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("❌ Error: Jinja2 library not installed.")
    print("   Run: pip install jinja2")
    sys.exit(1)

try:
    from ulid import ULID
except ImportError:
    print("❌ Error: python-ulid library not installed.")
    print("   Run: pip install python-ulid")
    sys.exit(1)

# Import the sample data
from data.sample_turbo_dpp import DPP_DATA


def normalize_dpp_id(dpp_id: str) -> str:
    """Use the Made2Verify-style dpp_ prefix while accepting raw ULIDs."""
    return dpp_id if dpp_id.startswith("dpp_") else f"dpp_{dpp_id}"


def generate_dpp_id(base_data=None) -> str:
    """Return a deterministic DPP ID unless a caller asks for a fresh one."""
    explicit_dpp_id = os.environ.get("DPP_ID") or (base_data or {}).get("dpp_id")
    generate_new = os.environ.get("DPP_GENERATE_NEW", "").lower() in {"1", "true", "yes"}

    if explicit_dpp_id and not generate_new:
        return normalize_dpp_id(explicit_dpp_id)

    return normalize_dpp_id(str(ULID()))


def generate_qr_code(data: str, error_correction: int = ERROR_CORRECT_H) -> tuple:
    """
    Generate a QR code from the provided data string.

    Returns:
        tuple: (base64_encoded_png, PIL.Image)
    """
    qr = qrcode.QRCode(
        version=None,  # Auto-determine version
        error_correction=error_correction,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert to base64 for inline embedding
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    qr_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return qr_b64, img


def image_to_data_uri(image_path: str | None) -> str:
    """Embed a local product image so generated passports stay self-contained."""
    if not image_path:
        return ""

    path = Path(image_path)
    if not path.exists():
        return ""

    mime_type, _ = mimetypes.guess_type(path.name)
    mime_type = mime_type or "image/jpeg"
    image_b64 = base64.b64encode(path.read_bytes()).decode("utf-8")

    return f"data:{mime_type};base64,{image_b64}"


def prepare_data(dpp_data: dict, dpp_id: str) -> dict:
    """
    Prepare the DPP data by injecting the generated ULID and updating the passport URL.

    Args:
        dpp_data: The base DPP data dictionary
        dpp_id: The generated ULID

    Returns:
        dict: The prepared data with updated fields
    """
    data = json.loads(json.dumps(dpp_data))  # Deep copy

    # Update with generated ULID
    data["dpp_id"] = dpp_id

    # Update passport URL with the actual ULID. In GitHub Actions, derive the
    # Pages URL from the repository so forks/repo renames deploy correctly.
    explicit_base_url = os.environ.get("DPP_BASE_URL")
    github_repository = os.environ.get("GITHUB_REPOSITORY")

    if explicit_base_url:
        base_url = explicit_base_url.rstrip("/")
    elif github_repository and "/" in github_repository:
        owner, repo = github_repository.split("/", 1)
        base_url = f"https://{owner}.github.io/{repo}"
    else:
        base_url = data["passport_url"].split("/{")[0].rstrip("/")

    data["passport_url"] = f"{base_url}/{dpp_id}/"

    return data


def intcomma_filter(value):
    """
    Convert an integer to a string with thousands separators.
    e.g., 180000 -> "180,000"
    """
    try:
        value = int(value)
        return f"{value:,}"
    except (ValueError, TypeError):
        return str(value)


def render_template(data: dict, qr_b64: str, template_path: str = "templates") -> str:
    """
    Render the Jinja2 template with the provided data.

    Args:
        data: The DPP data dictionary
        qr_b64: Base64-encoded QR code PNG
        template_path: Path to the templates directory

    Returns:
        str: Rendered HTML content
    """
    env = Environment(
        loader=FileSystemLoader(template_path),
        autoescape=True,
    )

    # Register custom filters
    env.filters['intcomma'] = intcomma_filter

    template = env.get_template("dpp_template.html")

    # Prepare JSON for the raw data view
    dpp_json = json.dumps(data, indent=2, ensure_ascii=False)

    html_content = template.render(
        dpp=data,
        qr_code_b64=qr_b64,
        product_image_data_uri=image_to_data_uri(data.get("product", {}).get("image_path")),
        dpp_json=dpp_json,
    )

    return html_content


def save_output(html_content: str, filename: str, output_dir: str = "output") -> str:
    """
    Save the generated HTML to a file.

    Args:
        html_content: The HTML content to save
        filename: The output filename
        output_dir: The output directory path

    Returns:
        str: Full path to the saved file
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    return filepath


def save_qr_label(qr_image, tracking_id: str, output_dir: str = "output") -> str:
    """
    Save the QR code as a standalone PNG for physical label printing.

    Args:
        qr_image: PIL Image object of the QR code
        tracking_id: The tracking ID to include in the filename
        output_dir: The output directory path

    Returns:
        str: Full path to the saved file
    """
    os.makedirs(output_dir, exist_ok=True)
    filename = f"label_{tracking_id}.png"
    filepath = os.path.join(output_dir, filename)

    qr_image.save(filepath, format="PNG")

    return filepath


def save_pages_routes(html_content: str, dpp_id: str, output_dir: str = "output") -> tuple:
    """
    Save GitHub Pages-friendly routes.

    The root index gives visitors a default page, while /{dpp_id}/ matches the
    QR code URL embedded in the passport.
    """
    root_index_path = save_output(html_content, "index.html", output_dir)
    dpp_index_path = save_output(html_content, "index.html", os.path.join(output_dir, dpp_id))

    return root_index_path, dpp_index_path


def main():
    """Main entry point for the DPP generator."""
    print("🔧 Digital Product Passport Generator")
    print("=" * 50)

    # Step 1: Resolve DPP identifier
    print("\n📋 Resolving unique DPP identifier...")
    dpp_id = generate_dpp_id(DPP_DATA)
    print(f"   DPP ID: {dpp_id}")

    # Step 2: Prepare data
    print("\n📊 Preparing DPP data...")
    data = prepare_data(DPP_DATA, dpp_id)
    tracking_id = data["remanufactured_unit"]["tracking_id"]
    print(f"   Tracking ID: {tracking_id}")
    print(f"   Passport URL: {data['passport_url']}")

    # Step 3: Generate QR code
    print("\n📱 Generating QR code...")
    qr_b64, qr_image = generate_qr_code(data["passport_url"])
    print(f"   QR code generated ({len(qr_b64)} chars base64)")

    # Step 4: Render template
    print("\n🎨 Rendering HTML template...")
    html_content = render_template(data, qr_b64)
    html_size = len(html_content)
    print(f"   HTML size: {html_size:,} characters")

    # Step 5: Save outputs
    print("\n💾 Saving output files...")
    html_filename = f"dpp_{tracking_id}.html"
    html_path = save_output(html_content, html_filename)
    print(f"   ✅ HTML saved: {html_path}")

    root_index_path, dpp_index_path = save_pages_routes(html_content, dpp_id)
    print(f"   ✅ Pages root saved: {root_index_path}")
    print(f"   ✅ Pages DPP route saved: {dpp_index_path}")

    label_path = save_qr_label(qr_image, tracking_id)
    print(f"   ✅ QR label saved: {label_path}")

    # Summary
    print("\n" + "=" * 50)
    print("🎉 DPP Generation Complete!")
    print("=" * 50)
    print(f"\n📄 HTML Passport: {html_path}")
    print(f"🏷️  QR Label: {label_path}")
    print(f"🔗 Passport URL: {data['passport_url']}")
    print(f"📅 Generated: {data['issued_date']}")
    print(f"\n💡 Next steps:")
    print(f"   1. Open {html_path} in a browser to preview")
    print(f"   2. Print {label_path} for physical labeling")
    print(f"   3. Deploy HTML to GitHub Pages or similar hosting")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"\n❌ File not found error: {e}")
        print("   Make sure you're running this from the project root directory.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
