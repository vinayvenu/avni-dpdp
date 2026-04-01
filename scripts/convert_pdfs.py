#!/usr/bin/env python3
"""Convert all PDFs in the repository to Markdown, retaining images/graphs.

Uses marker-pdf for high-quality conversion with layout and image preservation.
Output mirrors the source directory structure under a sibling `markdown/` folder.
Images are saved alongside the markdown file in an `images/` subdirectory.
"""

import os
import shutil
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
OUTPUT_ROOT = REPO_ROOT / "markdown"


def find_pdfs():
    return sorted(REPO_ROOT.rglob("*.pdf"))


def output_path_for(pdf: Path) -> Path:
    """Mirror the PDF's relative path under OUTPUT_ROOT, with .md extension."""
    rel = pdf.relative_to(REPO_ROOT)
    return OUTPUT_ROOT / rel.with_suffix(".md")


def convert(pdf: Path, out_md: Path):
    # Import here so errors surface per-file
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered

    out_md.parent.mkdir(parents=True, exist_ok=True)
    images_dir = out_md.parent / "images" / out_md.stem

    models = create_model_dict()
    converter = PdfConverter(artifact_dict=models)
    rendered = converter(str(pdf))
    md_text, _, images = text_from_rendered(rendered)

    # Save images
    if images:
        images_dir.mkdir(parents=True, exist_ok=True)
        for img_name, img in images.items():
            img.save(images_dir / img_name)
        # Rewrite image paths in markdown to be relative
        md_text = md_text.replace("![", "![").replace(
            "](", "]("  # no-op placeholder; paths below
        )
        # marker writes paths like `img_name` — prefix with relative images dir
        rel_images = f"images/{out_md.stem}"
        for img_name in images:
            md_text = md_text.replace(f"]({img_name})", f"]({rel_images}/{img_name})")

    out_md.write_text(md_text, encoding="utf-8")
    return len(images) if images else 0


def main():
    pdfs = find_pdfs()
    print(f"Found {len(pdfs)} PDFs\n")

    for pdf in pdfs:
        out_md = output_path_for(pdf)
        rel = pdf.relative_to(REPO_ROOT)

        if out_md.exists():
            print(f"[skip]    {rel}  (already converted)")
            continue

        print(f"[convert] {rel} ...", end=" ", flush=True)
        try:
            n_images = convert(pdf, out_md)
            status = f"done ({n_images} images)" if n_images else "done"
            print(status)
        except Exception as e:
            print(f"ERROR: {e}", file=sys.stderr)

    print("\nAll done. Markdown files are in:", OUTPUT_ROOT)


if __name__ == "__main__":
    main()
