import argparse
import sys
from rich.console import Console

from . import __version__
from . import config
from .storage import (
    create_note,
    edit_note,
    delete_note,
    list_notes,
    set_status,
    get_note_path,
)
from .storage.backup import backup_notes
from .exporters import export_html, export_pdf
from .utils.editor import launch_editor  # (used indirectly via storage functions)

# ----------------------------------------------------------------------
# Helper: build the argument parser
# Defines CLI structure, available commands, and their arguments.
# ----------------------------------------------------------------------
def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="notes",
        description="Simple Neovim-based Notes CLI",
    )
    # Global flags
    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        help="Show the installed notes version and exit",
    )

    # Subcommands container
    sub = parser.add_subparsers(dest="command", required=False)

    # ----- add ---------------------------------------------------------
    # Create a new note with a required title
    add = sub.add_parser("add", help="Add a new note")
    add.add_argument("--title", required=True, help="Title of the note")

    # ----- edit --------------------------------------------------------
    # Open an existing note in the editor
    edit = sub.add_parser("edit", help="Edit an existing note")
    edit.add_argument("--title", required=True, help="Title of the note")

    # ----- delete ------------------------------------------------------
    # Delete an existing note
    delete = sub.add_parser("delete", help="Delete a note")
    delete.add_argument("--title", required=True, help="Title of the note")

    # ----- list --------------------------------------------------------
    # List all notes with metadata (titles, statuses, etc.)
    sub.add_parser("list", help="List all notes")

    # ----- status ------------------------------------------------------
    # Change the status of a note (open, in progress, done)
    status = sub.add_parser("status", help="Change a note's status")
    status.add_argument("--title", required=True, help="Title of the note")
    status.add_argument(
        "--set",
        required=True,
        choices=["open", "in progress", "done"],
        help="New status",
    )

    # ----- export ------------------------------------------------------
    # Export a single note or all notes into PDF/HTML formats
    export = sub.add_parser("export", help="Export notes")
    export.add_argument("--title", help="Title of a single note (omit for --all)")
    export.add_argument("--pdf", action="store_true", help="Export as PDF")
    export.add_argument("--html", action="store_true", help="Export as HTML")
    export.add_argument("--all", action="store_true", help="Export all notes")

    # ----- backup ------------------------------------------------------
    # Backup all notes into a ZIP archive
    sub.add_parser("backup", help="Create a ZIP backup of all notes")

    return parser


# ----------------------------------------------------------------------
# Main entry point called from the console-script
# Handles parsing, dispatch, and execution of CLI commands.
# ----------------------------------------------------------------------
def run(argv=None) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)

    # --------------------------------------------------------------
    # Version shortcut: print version and exit immediately
    # --------------------------------------------------------------
    if getattr(args, "version", False):
        console = Console()
        console.print(f"[bold]notes[/bold] version {__version__}")
        return

    # --------------------------------------------------------------
    # If no sub-command was provided, print help message
    # --------------------------------------------------------------
    if args.command is None:
        parser.print_help()
        return

    # --------------------------------------------------------------
    # Dispatch subcommands to their respective implementations
    # --------------------------------------------------------------
    if args.command == "add":
        create_note(args.title)

    elif args.command == "edit":
        edit_note(args.title)

    elif args.command == "delete":
        delete_note(args.title)

    elif args.command == "list":
        list_notes()

    elif args.command == "status":
        set_status(args.title, args.set)

    elif args.command == "export":
        if args.all:
            # Export every note in the requested formats
            for note_file in config.NOTES_DIR.glob("*.md"):
                title = note_file.stem.replace("_", " ")
                _export_one(title, args.pdf, args.html)
        elif args.title:
            # Export a single specified note
            _export_one(args.title, args.pdf, args.html)
        else:
            # Error: user didn’t specify --title or --all
            console = Console()
            console.print(
                "[red]Error:[/red] Provide --title or --all.", style="red", file=sys.stderr
            )

    elif args.command == "backup":
        # Create a ZIP archive containing all notes
        backup_notes()


# ----------------------------------------------------------------------
# Helper: export a single note
# Reads a note, converts it into the requested formats (PDF/HTML),
# and prints coloured feedback messages.
# ----------------------------------------------------------------------
def _export_one(title: str, pdf: bool, html: bool) -> None:
    console = Console()
    note_path = get_note_path(title)

    # Check if note exists
    if not note_path.exists():
        console.print(f"[red]Error:[/red] Note '{title}' not found.", style="red")
        return

    # Read note content as markdown
    markdown_text = note_path.read_text(encoding="utf-8")

    # Export to HTML if requested
    if html:
        out_path = export_html(title, markdown_text)
        console.print(f"[green]Exported HTML:[/green] {out_path}")

    # Export to PDF if requested
    if pdf:
        out_path = export_pdf(title, markdown_text)
        console.print(f"[green]Exported PDF:[/green] {out_path}")
