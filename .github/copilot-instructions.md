## Purpose

This file contains short, actionable guidance for AI coding agents working on this repository.
Use it to quickly understand the repository's shape, how to run things, and the small, explicit conventions discovered here.

## Repo snapshot & big picture

- Root contains a single script: `first code.py` (Python). No packages, no tests, no CI config detected.
- `first code.py` (line 1) contains: `print('Hello World!')` — this repo is currently a minimal single-file Python script.

## How to run (Windows PowerShell)

Run the script directly with the user's default shell (PowerShell):

```powershell
python "first code.py"
```

If you add dependencies, prefer a virtual environment and `requirements.txt`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## What an AI agent should assume and prioritize

- This is a micro-repo: prefer small, focused changes that preserve the single-file layout unless the user asks for a package.
- There is no existing test suite or CI; if you add tests, also add a minimal `README.md` and `requirements.txt` so humans can reproduce your run locally.
- Be conservative when renaming `first code.py` — it includes a space in the filename. If you refactor to `first_code.py`, update any documentation and references accordingly.

## Project-specific conventions (discoverable)

- Filenames: currently one file uses a space — treat filenames as literal and quote them in run commands.
- Python version: not specified. Target a modern Python 3.x runtime (3.8+) unless the user asks otherwise.

## Integration points and dependencies

- None detected. No external services, packages, or network calls found.

## Examples of actionable assistant tasks

- Add a README explaining the script and how to run it.
- Replace `print('Hello World!')` with a small CLI using `argparse` if asked to add features; include tests under `tests/` and a `requirements.txt` if external packages are used.
- If you split this into a package, add `pyproject.toml` or `setup.cfg` and keep backwards-compatible entry points.

## Merge/update guidance

- If `.github/copilot-instructions.md` already exists, merge by preserving any human-written guidance and keep the "How to run" commands accurate for Windows PowerShell.
- Avoid removing the note about the filename containing a space without confirming with the repo owner.

## Questions for the repo owner

- Do you want this to remain a single-script repo, or should agents propose a package layout when adding features? Reply with preferred structure (single-file / module / package).

---
If anything here is unclear or you'd like me to expand any section (examples, CI, tests, or a suggested package layout), tell me which part to iterate on.
