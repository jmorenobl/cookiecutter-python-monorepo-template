#!/usr/bin/env python
import os
import shutil
import subprocess
from pathlib import Path


def main():
    # Create basic directory structure
    for dir_name in ["apps", "libs", "tools"]:
        os.makedirs(dir_name, exist_ok=True)

    # Initialize UV environment and install just
    subprocess.run(["uv", "sync"], check=True)

    # Create a just wrapper script in tools directory
    tools_dir = Path("tools")
    with open(tools_dir / "just", "w", encoding="utf-8") as f:
        f.write("#!/bin/bash\nuv run just \"$@\"")
    
    # Make it executable
    os.chmod(tools_dir / "just", 0o755)
    
    # Remove .gitkeep files
    for dir_name in ["apps", "libs", "tools"]:
        gitkeep = Path(dir_name) / ".gitkeep"
        if gitkeep.exists():
            gitkeep.unlink()

    # Remove .vscode directory if not needed
    if "{{ cookiecutter.use_vscode }}" != "yes":
        vscode_dir = Path(".vscode")
        if vscode_dir.exists():
            for file in vscode_dir.glob("*"):
                file.unlink()
            vscode_dir.rmdir()


if __name__ == "__main__":
    main()
