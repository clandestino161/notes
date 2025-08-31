# CLI Notes

A simple Neovim-based note-taking CLI application with Markdown support, note management, export to HTML/PDF, and backup functionality.

---

## Requirements (for development)

* Python 3.8+ (only if building from source)
* Neovim installed (or any $EDITOR for editing notes)
* Git installed (for cloning the repository)

---

## Installation (End Users)

You can download pre-built binaries for your system from the [Releases page](https://github.com/clandestino161/notes/releases).

### Linux

1. Download the Linux binary `notes-linux`.
2. Make it executable:

```bash
chmod +x notes-linux
```

3. Move it to a directory in your PATH, e.g.:

```bash
sudo mv notes-linux /usr/local/bin/notes
```

4. Run it:

```bash
notes add --title "My First Note"
```

### macOS

1. Download the macOS binary `notes-macos`.
2. Make it executable:

```bash
chmod +x notes-macos
```

3. Move it to a directory in your PATH, e.g.:

```bash
sudo mv notes-macos /usr/local/bin/notes
```

4. Run it:

```bash
notes list
```

### Windows

1. Download the Windows binary `notes-windows.exe`.
2. Move it to a folder in your PATH (e.g., `C:\Windows\System32` or any folder added to PATH).
3. Run it from Command Prompt or PowerShell:

```powershell
notes.exe add --title "My First Note"
```

---

## Features

* Create notes in Markdown from the CLI and open them directly in Neovim (or default \$EDITOR)
* Set a status (`open`, `in progress`, `done`) for each note (default: `open`)
* Modify notes directly in your editor
* Access all notes from anywhere
* Delete notes
* List notes with Title, Status, and Last Modified date
* Export notes individually or all at once to HTML/PDF in the user’s Downloads directory
* Backup all notes as a ZIP archive in the user’s Downloads directory

---

## Usage

All commands can be run from anywhere after installation.

### Add a new note

```bash
notes add --title "Title of the Note"
```

### Edit a note

```bash
notes edit --title "Title of the Note"
```

### Delete a note

```bash
notes delete --title "Title of the Note"
```

### List all notes

Shows all saved notes without opening them:

```bash
notes list
```

┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Title       ┃ Status       ┃ Last Modified   ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ First Note  │ open         │ 2025-08-24 12:42│
│ Second Note │ in progress  │ 2025-08-24 13:10│
│ Done Note   │ done         │ 2025-08-24 14:05│
└─────────────┴──────────────┴─────────────────┘

### Change status of an existing note

```bash
notes status --title "Title of the Note" --set "in progress"
notes status --title "Title of the Note" --set "done"
```

### Export notes

Export a single note:

```bash
notes export --title "First Note" --pdf --html
```

Export all notes:

```bash
notes export --all --pdf --html
```

### Backup all notes

```bash
notes backup
```

---

## Notes Directory

All notes are stored in a standard location:

```bash
~/.local/share/notes
```

The directory is created automatically on first run.

---

## Uninstallation

Remove the binary from your PATH:

```bash
# Linux/macOS
sudo rm /usr/local/bin/notes

# Windows
# Delete notes.exe from your PATH folder
```

Optionally, delete all saved notes (⚠ irreversible):

```bash
rm -rf ~/.local/share/notes
```

---

## Development (Optional)

To build from source:

```bash
git clone https://github.com/clandestino161/notes.git
cd notes
python3 -m pip install -r requirements.txt
python3 src/notes/main.py add --title "Test Note"
```

---

## License

MIT
