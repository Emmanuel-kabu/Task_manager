# Contributing to TaskFlow

## Development Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
4. Install dependencies: `pip install -r requirements.txt`

## Running Tests

```bash
pytest tests/ -v
```

## Code Style

- Use clear, descriptive function and variable names
- Add docstrings to all public functions
- Follow PEP 8 conventions

## Commit Guidelines

- One logical change per commit
- Use clear, descriptive commit messages
- Reference the user story ID in the commit message (e.g., "US1: ...")

## Branch Strategy

- `main` is the primary branch
- All changes go through CI before merging
