


# Development
To develop 
```bash
uv self update
uv python install 3.14
uv venv
. .venv/Scripts/activate
uv pip install -r pyproject.toml
uv sync
uv pip install -e .
uv run src/data_preprocessor
```

