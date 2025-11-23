
- **Website:** https://projects.vannijnatten.dev/dpp
- **Documentation:** https://projects.vannijnatten.dev/dpp/docs


Code of Conduct
----------------------

The Data Processor is an open source project developed by a lonely developer in need of contributors. Please read how to
[Contribute](./docs/CONTRIBUTING.md). Please also read the [Code of Conduct](./docs/CODE_OF_CONDUCT.md) for guidance on
how to interact with others in a way that makes a community thrive.


Development
----------------------


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


Testing
----------------------

NumPy requires `pytest`.


Call for Contributions
----------------------

Writing code isn’t the only way to contribute. You can also:
- review pull requests
- help us stay on top of new and old issues
- develop tutorials, presentations, and other educational materials
- develop graphic design for our brand assets and promotional materials
- translate website content
- help with outreach and onboard new contributors
- write grant proposals and help with other fundraising efforts

If you are new to contributing to open source, [this
guide](https://opensource.guide/how-to-contribute/) helps explain why, what,
and how to successfully get involved.
