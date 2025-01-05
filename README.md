# Cookiecutter Monorepo Template

A Cookiecutter template for creating Python monorepo projects with apps and libraries, using modern tools like `uv` for dependency management and `just` for task automation.

## Features

- Modern Python monorepo structure with apps and libraries
- UV for dependency management
- Just for task automation
- Ruff for linting and formatting
- Optional VSCode configuration
- Initial app and library structure

## Requirements

- Python 3.11 or higher
- Cookiecutter
- UV package manager
- Just command runner (Rust-based)

## Usage

```bash
cookiecutter gh:your-username/cookiecutter-monorepo-template
```

## Template Options

- `project_name`: Name of your project
- `project_slug`: Slug version of your project name (auto-generated)
- `project_description`: Brief description of your project
- `python_version`: Python version to use (3.11 minimum)
- `author_name`: Your name
- `author_email`: Your email
- `initial_app_name`: Name of the initial app to create
- `initial_lib_name`: Name of the initial library to create
- `use_vscode`: Whether to include VSCode configuration

## Project Structure

The generated project will have the following structure:

```
your-project/
├── apps/
│   └── initial-app/
├── libs/
│   └── initial-lib/
├── tools/
├── .vscode/           # Optional
├── pyproject.toml
├── justfile
├── .gitignore
└── README.md
```

## License

This project is licensed under the MIT License. 