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

    # Copy justfile from templates
    template_dir = Path(os.environ.get("COOKIECUTTER_TEMPLATE_DIR", os.getcwd())).absolute()
    
    if template_dir.exists():
        # Look for justfile in the correct location
        possible_paths = [
            template_dir.parent.parent / "templates" / "justfile",  # Go up two levels
            template_dir.parent / "templates" / "justfile",  # Go up one level
            Path("templates") / "justfile",  # Try relative to current directory
            template_dir / "templates" / "justfile",
            template_dir / "justfile"
        ]
        
        for justfile_template in possible_paths:
            justfile_template = justfile_template.absolute()
            if justfile_template.exists():
                shutil.copy(str(justfile_template), "justfile")
                break
        else:
            print("Warning: Could not find justfile in template directories")
    else:
        print(f"Template directory does not exist: {template_dir}")

    # Remove .vscode directory if not needed
    if "{{ cookiecutter.use_vscode }}" != "yes":
        vscode_dir = Path(".vscode")
        if vscode_dir.exists():
            for file in vscode_dir.glob("*"):
                file.unlink()
            vscode_dir.rmdir()


if __name__ == "__main__":
    main()
