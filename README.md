# CLI Notes

A CLI note‑taking tool that opens notes in your preferred editor (defaults to Neovim) with Markdown support, note management, export to HTML/PDF, and backup functionality.

---

## Installation

Pre‑built binaries are provided on the **Releases** page.

1. **Download the binary** (`notes-linux.zip`).
2. Extract the zip file:

```bash
unzip notes-linux.zip
```

3. Chnage dictionary

```bash
cd dist
```

4. Make the binary executable:

```bash
chmod +x notes
```

5. Move it to a directory that’s on your $PATH:

```bash
sudo mv notes /usr/local/bin/notes
```

6. Run the program:

```bash
notes add --title "My First Note"
```

## Features

* Create notes in Markdown from the CLI and open them directly in your preferred editor (defaults to Neovim)
* Assign a status (open, in progress, done) to each note (default: open)
* Edit notes directly in your editor
* List notes with title, status, and last‑modified timestamp
* Delete notes securely
* Export notes individually or all at once to HTML and/or PDF (saved to ~/Downloads)
* Backup all notes as a ZIP archive (saved to ~/Downloads)

## Usage

All commands can be run from anywhere after the binary is installed.

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

### Change the status of an existing note

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

## Notes Directory

All notes are stored in a standard location that is created automatically on first use (or during package installation):

```bash
~/.local/share/notes
```

## Uninstallation

Remove the binary from your $PATH:

```bash
sudo rm /usr/local/bin/notes
```

Optionally, delete all saved notes (⚠️ irreversible):

```bash
rm -rf ~/.local/share/notes
```

License
MIT © 2025 clandestino161
