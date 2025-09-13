import datetime
from pathlib import Path
from ..config import NOTES_DIR, DEFAULT_STATUS, STATUS_COMMENT_TEMPLATE


class Note:
    """
    Representation of a note stored as a Markdown file.

    A note consists of:
    - A status comment on the first line (e.g., <!-- status: open -->).
    - A Markdown body (typically starting with a heading).
    """

    def __init__(self, title: str):
        # Human-readable title (with spaces)
        self.title = title

        # File system path derived from the title
        self.path = self._path_from_title(title)

        # Raw note content loaded from disk
        self.content: str = ""

        # Current status (default = "open")
        self.status: str = DEFAULT_STATUS

    # ------------------------------------------------------------------
    # Helpers for filename ↔ title conversion
    # ------------------------------------------------------------------
    @staticmethod
    def _sanitize(title: str) -> str:
        """
        Convert a note title into a safe filename.

        Example:
            "My Note" → "My_Note.md"
        """
        return f"{title}.md".replace(" ", "_")

    @classmethod
    def _path_from_title(cls, title: str) -> Path:
        """
        Build a full Path object for a note given its title.
        """
        return NOTES_DIR / cls._sanitize(title)

    # ------------------------------------------------------------------
    # Load / save helpers
    # ------------------------------------------------------------------
    def load(self) -> None:
        """
        Load the note from disk.

        - Reads the Markdown file.
        - Extracts the current status from the first line.
        """
        self.content = self.path.read_text(encoding="utf-8")
        self.status = self._extract_status(self.content)

    def save(self) -> None:
        """
        Save the note back to disk.

        - Ensures the status comment is always present as the first line.
        - Preserves the existing body (stripping leading whitespace).
        """
        header = STATUS_COMMENT_TEMPLATE.format(self.status)
        # Strip leading whitespace so status is guaranteed on top
        body = self.content.lstrip()
        self.path.write_text(header + body, encoding="utf-8")

    # ------------------------------------------------------------------
    # Status handling
    # ------------------------------------------------------------------
    @staticmethod
    def _extract_status(text: str) -> str:
        """
        Parse a Markdown text to find the status line.

        Expected format:
            <!-- status: <value> -->
        Falls back to DEFAULT_STATUS if not found.
        """
        for line in text.splitlines():
            if line.startswith("<!-- status:"):
                return (
                    line.replace("<!-- status:", "")
                    .replace("-->", "")
                    .strip()
                )
        return DEFAULT_STATUS

    def set_status(self, new_status: str) -> None:
        """
        Update the note’s status both in memory and in its text content.
        """
        self.status = new_status

        # Split into lines to adjust the first one if it’s a status line
        lines = self.content.splitlines()

        if lines and lines[0].startswith("<!-- status:"):
            # Replace existing status line
            lines[0] = STATUS_COMMENT_TEMPLATE.format(new_status).strip()
        else:
            # Prepend status if missing
            lines.insert(0, STATUS_COMMENT_TEMPLATE.format(new_status).strip())

        # Reassemble with trailing newline
        self.content = "\n".join(lines) + "\n"
