import os
import subprocess
from rich.console import Console

# Rich console instance for styled error messages
console = Console()


# ----------------------------------------------------------------------
# Launch an external editor
# ----------------------------------------------------------------------
def launch_editor(file_path):
    """
    Open a file in the user’s preferred editor.

    Editor selection:
    - First tries $EDITOR environment variable (default: "nvim").
    - Falls back to "nvim" if $EDITOR is not set.

    Parameters
    ----------
    file_path : str | Path
        Path to the file that should be opened in the editor.

    Error handling
    --------------
    - FileNotFoundError: editor binary does not exist on the system.
    - CalledProcessError: editor was launched but exited with a non-zero code.
    """
    editor = os.getenv("EDITOR", "nvim")

    try:
        # Launch the editor with the file
        subprocess.run([editor, str(file_path)], check=True)

    except FileNotFoundError:
        # Case: user’s chosen editor does not exist
        console.print(
            f"[red]Error:[/red] Editor '{editor}' not found. "
            "Set the $EDITOR environment variable to a valid program."
        )

    except subprocess.CalledProcessError as exc:
        # Case: editor ran but exited abnormally
        console.print(
            f"[red]Error:[/red] Editor exited with status {exc.returncode}"
        )
