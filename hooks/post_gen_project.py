#!/usr/bin/env python
import os
import shutil
import subprocess
from pathlib import Path


def main():
    # Create basic directory structure
    for dir_name in ["apps", "libs", "tools"]:
        os.makedirs(dir_name, exist_ok=True)

    # Initialize UV environment
    subprocess.run(["uv", "venv"], check=True)

    # Create initial app and lib structure
    app_name = "{{ cookiecutter.initial_app_name }}"
    lib_name = "{{ cookiecutter.initial_lib_name }}"

    # Create app directory
    app_dir = Path("apps") / app_name
    app_dir.mkdir(parents=True, exist_ok=True)
    (app_dir / "src").mkdir(exist_ok=True)
    (app_dir / "tests").mkdir(exist_ok=True)
    (app_dir / "src" / "__init__.py").touch()
    (app_dir / "tests" / "__init__.py").touch()

    # Create lib directory
    lib_dir = Path("libs") / lib_name
    lib_dir.mkdir(parents=True, exist_ok=True)
    (lib_dir / "src").mkdir(exist_ok=True)
    (lib_dir / "tests").mkdir(exist_ok=True)
    (lib_dir / "src" / "__init__.py").touch()
    (lib_dir / "tests" / "__init__.py").touch()

    # Copy justfile from templates
    template_dir = Path(os.environ.get("COOKIECUTTER_TEMPLATE_DIR", ""))
    if template_dir.exists():
        justfile_template = template_dir / "templates" / "justfile"
        if justfile_template.exists():
            shutil.copy(str(justfile_template), "justfile")

    # Remove .vscode directory if not needed
    if "{{ cookiecutter.use_vscode }}" != "yes":
        vscode_dir = Path(".vscode")
        if vscode_dir.exists():
            for file in vscode_dir.glob("*"):
                file.unlink()
            vscode_dir.rmdir()


if __name__ == "__main__":
    main()
