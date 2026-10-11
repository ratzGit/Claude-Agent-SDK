import os
import sys

from importlib.metadata import PackageNotFoundError, version

LOGO = r"""
            _   _       _
  _ __ __ _| |_| | __ _| |__
 | '__/ _` | __| |/ _` | '_ \
 | | | (_| | |_| | (_| | |_) |
 |_|  \__,_|\__|_|\__,_|_.__/
"""

GRADIENT = [45, 44, 43, 42, 41, 40]


def _supports_color() -> bool:
    if os.environ.get("NO_COLOR") or not sys.stdout.isatty():
        return False
    if os.name == "nt":
        # Enables ANSI escape processing in the legacy Windows console.
        os.system("")
    return True


def _version() -> str:
    try:
        return version("ratlab")
    except PackageNotFoundError:
        return "dev"


def show_splash() -> None:
    color = _supports_color()
    lines = LOGO.strip("\n").splitlines()
    for i, line in enumerate(lines):
        if color:
            code = GRADIENT[i % len(GRADIENT)]
            print(f"\033[1;38;5;{code}m{line}\033[0m")
        else:
            print(line)

    tagline = f"  experiments with the Claude Agent SDK  -  v{_version()}"
    print(f"\033[2m{tagline}\033[0m" if color else tagline)
    print()
