import datetime
from pathlib import Path
from typing import List

from rich.console import Console
from rich.table import Table

from ..config import NOTES_DIR, DOWNLOADS_DIR, DEFAULT_STATUS, STATUS_COMMENT_TEMPLATE
from ..models.note import Note

# Console instance for styled terminal output
console = Console()


# ----------------------------------------------------------------------
# Path handling
# ----------------------------------------------------------------------
def get_note_path(title: str) -> Path:
    """
    Compute the filesystem path for a note based on its title.
    Spaces are replaced with underscores and `.md` is appended.
    """
    return NOTES_DIR / f"{title}.md".replace(" ", "_")


# ----------------------------------------------------------------------
# Note creation
# ----------------------------------------------------------------------
def create_note(title: str) -> None:
    """
    Create a new note with the given title.

    - Initializes the file with a default status comment
      and a Markdown level-1 heading.
    - Opens the note immediately in the configured editor.
    """
    note_path = get_note_path(title)

    if note_path.exists():
        console.print(f"[red]Error:[/red] Note '{title}' already exists.")
        return

    # Initialize the new note with status + heading
    note_path.write_text(
        f"{STATUS_COMMENT_TEMPLATE.format(DEFAULT_STATUS)}# {title}\n\n",
        encoding="utf-8",
    )
    console.print(f"[green]Created note:[/green] {title}")

    # Open in the editor (lazy import avoids circular dependency)
    from ..utils.editor import launch_editor
    launch_editor(note_path)


# ----------------------------------------------------------------------
# Note editing
# ----------------------------------------------------------------------
def edit_note(title: str) -> None:
    """
    Open an existing note in the user’s editor.
    """
    note_path = get_note_path(title)

    if not note_path.exists():
        console.print(f"[red]Error:[/red] Note '{title}' not found.")
        return

    from ..utils.editor import launch_editor
    launch_editor(note_path)


# ----------------------------------------------------------------------
# Note deletion
# ----------------------------------------------------------------------
def delete_note(title: str) -> None:
    """
    Delete a note permanently.
    """
    note_path = get_note_path(title)

    if not note_path.exists():
        console.print(f"[red]Error:[/red] Note '{title}' not found.")
        return

    note_path.unlink()
    console.print(f"[green]Deleted:[/green] {title}")


# ----------------------------------------------------------------------
# Listing notes
# ----------------------------------------------------------------------
def list_notes() -> None:
    """
    Display all notes in a formatted table, showing:
    - Title
    - Current status
    - Last modification time
    """
    md_files: List[Path] = sorted(
        p for p in NOTES_DIR.iterdir() if p.suffix == ".md"
    )

    if not md_files:
        console.print("[yellow]No notes found.[/yellow]")
        return

    # Create a Rich table for pretty display
    table = Table(title="Your Notes")
    table.add_column("Title", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("Last Modified", style="green")

    for path in md_files:
        # Load note metadata (status etc.)
        note = Note(title=path.stem.replace("_", " "))
        note.path = path
        note.load()

        # Format last modified timestamp
        mtime = datetime.datetime.fromtimestamp(
            path.stat().st_mtime
        ).strftime("%Y-%m-%d %H:%M")

        # Add a row with note details
        table.add_row(note.title, note.status, mtime)

    console.print(table)


# ----------------------------------------------------------------------
# Status updates
# ----------------------------------------------------------------------
def set_status(title: str, new_status: str) -> None:
    """
    Change the status of a given note (e.g., open → in progress).
    """
    note_path = get_note_path(title)

    if not note_path.exists():
        console.print(f"[red]Error:[/red] Note '{title}' not found.")
        return

    # Load the note, update its status, and save
    note = Note(title)
    note.path = note_path
    note.load()
    note.set_status(new_status)
    note.save()

    console.print(f"[green]Updated status:[/green] {title} → {new_status}")
