from pathlib import Path
from weasyprint import HTML

from ..config import DOWNLOADS_DIR
from .markdown_renderer import render_markdown_to_html

# ----------------------------------------------------------------------
# Minimal CSS for monospaced rendering in PDF
# Ensures code blocks, headings, and body text use a monospace font
# ----------------------------------------------------------------------
MONO_CSS = """
<style>
    body, p, li, h1, h2, h3, h4, h5, h6 { font-family: "Courier New", Courier, monospace; }
    pre, code { font-family: "Courier New", Courier, monospace; }
</style>
"""

# ----------------------------------------------------------------------
# Export a Markdown note as a PDF
# ----------------------------------------------------------------------
def export_pdf(title: str, markdown_text: str) -> Path:
    """
    Convert Markdown content into a PDF file.

    Parameters
    ----------
    title : str
        Title of the note (used to name the PDF file)
    markdown_text : str
        The Markdown content of the note

    Returns
    -------
    Path
        Path to the generated PDF file in the DOWNLOADS_DIR
    """
    # Convert Markdown to HTML first
    html_body = render_markdown_to_html(markdown_text)

    # Apply monospace CSS styling
    full_html = MONO_CSS + html_body

    # Generate filename from title
    filename = f"{title.replace(' ', '_')}.pdf"
    out_path = DOWNLOADS_DIR / filename

    # Write the HTML content to a PDF file
    HTML(string=full_html).write_pdf(str(out_path))

    return out_path
