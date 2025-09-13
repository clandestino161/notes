import markdown2

# ----------------------------------------------------------------------
# Convert Markdown text to HTML
# ----------------------------------------------------------------------
def render_markdown_to_html(markdown_text: str) -> str:
    """
    Render a Markdown string as HTML.

    Parameters
    ----------
    markdown_text : str
        The Markdown content to convert.

    Returns
    -------
    str
        HTML string generated from the Markdown.
    """
    # Use the markdown2 library to handle conversion
    return markdown2.markdown(markdown_text)
