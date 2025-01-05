# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Project Structure

This is a Python monorepo project that uses `uv` for dependency management and `just` for task automation. The project is organized into:

- `apps/`: Contains standalone applications
- `libs/`: Contains shared libraries
- `tools/`: Contains development and build tools

## Initial Setup

1. Install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

2. Install Just command runner:
   ```bash
   cargo install just
   ```

## Development Commands

- List available commands:
  ```bash
  just
  ```

- Create a new component (app or library):
  ```bash
  just create-component [app|lib] name [description]
  ```

## Project Information

- Author: {{ cookiecutter.author_name }}
- Contact: {{ cookiecutter.author_email }}
- Python Version: {{ cookiecutter.python_version }} 