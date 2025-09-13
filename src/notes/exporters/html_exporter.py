from pathlib import Path
from ..config import DOWNLOADS_DIR
from .markdown_renderer import render_markdown_to_html

# ----------------------------------------------------------------------
# Minimal CSS for monospace rendering in HTML
# Ensures that headings, body text, and code blocks use a monospace font
# ----------------------------------------------------------------------
MONO_CSS = """
<style>
    body, p, li, h1, h2, h3, h4, h5, h6 { font-family: "Courier New", Courier, monospace; }
    pre, code { font-family: "Courier New", Courier, monospace; }
</style>
"""

# ----------------------------------------------------------------------
# Export a Markdown note as an HTML file
# ----------------------------------------------------------------------
def export_html(title: str, markdown_text: str) -> Path:
    """
    Convert Markdown content into an HTML file with monospace styling.

    Parameters
    ----------
    title : str
        Title of the note (used to generate the HTML filename)
    markdown_text : str
        The Markdown content to convert

    Returns
    -------
    Path
        Path to the generated HTML file in the DOWNLOADS_DIR
    """
    # Convert Markdown to HTML
    html_body = render_markdown_to_html(markdown_text)

    # Apply monospace CSS
    full_html = MONO_CSS + html_body

    # Generate filename from the title
    filename = f"{title.replace(' ', '_')}.html"
    out_path = DOWNLOADS_DIR / filename

    # Write the HTML content to disk
    out_path.write_text(full_html, encoding="utf-8")

    return out_path
