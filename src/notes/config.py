import os
from pathlib import Path

# ----------------------------------------------------------------------
# Directories
# ----------------------------------------------------------------------

# User’s home directory (cross-platform)
HOME = Path.home()

# Default storage location for notes (~/.local/share/notes)
NOTES_DIR = HOME / ".local" / "share" / "notes"

# Default location to save exported files (e.g., PDFs/HTMLs)
DOWNLOADS_DIR = HOME / "Downloads"

# Ensure required directories exist when the module is imported
# (prevents runtime errors when creating or exporting notes)
NOTES_DIR.mkdir(parents=True, exist_ok=True)
DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)


# ----------------------------------------------------------------------
# Note status handling
# ----------------------------------------------------------------------

# Default status assigned to a new note
DEFAULT_STATUS = "open"

# Template used to embed note status in Markdown files
# Example: "<!-- status: open -->"
STATUS_COMMENT_TEMPLATE = "<!-- status: {} -->\n"
