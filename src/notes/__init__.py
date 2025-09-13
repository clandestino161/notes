from importlib import metadata

try:
    # When the package is installed (wheel, sdist, editable) this returns the
    # version that Hatch wrote into the distribution metadata.
    __version__: str = metadata.version(__name__)   # e.g. "1.2.3"
except metadata.PackageNotFoundError:               # pragma: no cover
    # Fallback for a source checkout where the package isn’t installed yet.
    __version__ = "0+unknown"

__all__ = ["__version__"]
