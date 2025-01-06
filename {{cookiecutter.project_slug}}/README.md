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
   uv sync
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

  This will create a new directory in the appropriate folder (apps or libs) and add it to the workspace.

   Example:
   ```bash
   just create-component app web-app "My web app"
   just create-component lib utils "My utils library"
   ```

## Project Information

- Author: {{ cookiecutter.author_name }}
- Contact: {{ cookiecutter.author_email }}
- Python Version: {{ cookiecutter.python_version }} 