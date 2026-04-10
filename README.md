# MathMentor (ProfessorSama)

MathMentor is a middle-school math tutoring project with two user-facing experiences:

- **Discord bot** for quick question-and-answer tutoring.
- **Dashboard web UI** (`dashboard.html`) for in-browser ask flow.

The backend is a local Flask API that routes tutoring requests through a shared tutor engine.

## What this repo currently includes

- A root launcher (`main.py`) to run API, bot, and mocked API tests.
- Flask API endpoints including:
  - `GET /health`
  - `POST /ask` (supports minimal `{ "question": "..." }` payload)
  - `POST /explain`
- Discord bot integration.
- Mocked API contract tests in `tests/test_api.py`.

## Single Source of Truth (SSOT)

To keep behavior consistent, core ownership is intentionally split:

- Tutor logic: `chris_tutor_bot/tutor.py`
- API behavior: `chris_tutor_bot/api.py`
- Dashboard ask flow: `dashboard.html`

## Quick start

```bash
pip install -r chris_tutor_bot/requirements.txt
python main.py api
```

For more implementation details, see `chris_tutor_bot/README.md` and `PRD.md`.
