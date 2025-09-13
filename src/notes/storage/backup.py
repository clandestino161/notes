import datetime
import zipfile
from pathlib import Path

from ..config import NOTES_DIR, DOWNLOADS_DIR
from ..utils.editor import console


# ----------------------------------------------------------------------
# Backup all notes into a ZIP archive
# ----------------------------------------------------------------------
def backup_notes() -> None:
    """
    Create a timestamped ZIP archive containing all Markdown notes.

    - Archive is stored in the user's Downloads directory.
    - Only files ending with `.md` inside NOTES_DIR are included.
    - A success message is printed with the number of notes backed up.
    """
    # Generate a unique name based on current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"notes_backup_{timestamp}.zip"
    backup_path = DOWNLOADS_DIR / backup_name

    # Counter for number of notes included
    count = 0

    # Create a new ZIP file (overwrite if exists)
    with zipfile.ZipFile(backup_path, "w") as zipf:
        for file in NOTES_DIR.iterdir():
            # Only include Markdown notes
            if file.suffix == ".md":
                # Write file with just its filename inside the archive
                zipf.write(file, arcname=file.name)
                count += 1

    # Print a styled success message
    console.print(
        f"[green]Backup created:[/green] {backup_path} ({count} notes)"
    )
