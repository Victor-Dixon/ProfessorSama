# Chris Tutor Bot

Chris Tutor Bot is a modular tutoring system with a Discord interface and a Flask API backend powered by local Ollama models.

## Architecture

```text
Discord Bot (bot.py + cogs)
        |
        v
Tutor Engine (tutor.py)  <-->  Ollama HTTP API
        ^
        |
Flask API (api.py)
```

The dashboard (`../dashboard.html`) can call `POST /ask` directly.

## Repository Structure

```text
chris_tutor_bot/
├── api.py
├── bot.py
├── tutor.py
├── questions.py
├── progress.py
├── requirements.txt
├── .env.example
└── cogs/
    ├── quiz.py
    ├── homework.py
    ├── progress.py
    └── help_cmd.py
```

## Setup

1. Install dependencies:

```bash
pip install -r chris_tutor_bot/requirements.txt
```

2. Install and start Ollama:

```bash
ollama pull llama3
ollama serve
```

3. Configure environment variables:

```bash
cp chris_tutor_bot/.env.example chris_tutor_bot/.env
```

4. Run from repo root with the simplified launcher:

```bash
python main.py api
```

5. Run Discord bot:

```bash
python main.py bot
```

6. Run mocked API tests:

```bash
python main.py test
```

> You can still run `python chris_tutor_bot/api.py` and `python chris_tutor_bot/bot.py` directly if preferred.

## API Endpoints

### `GET /health`
Returns server health and configured model.

### `POST /ask`
Primary homework-help endpoint.

Minimal request:

```json
{ "question": "3/4 + 1/2" }
```

Backward-compatible request:

```json
{
  "question": "3/4 + 1/2",
  "user_answer": "4/6",
  "correct_answer": "1.25"
}
```

### `POST /explain`
Structured explanation endpoint for quiz flows.

## SSOT

- Tutor prompt logic: `chris_tutor_bot/tutor.py`
- API contract and validation: `chris_tutor_bot/api.py`
- Dashboard ask behavior: `dashboard.html`

## Testing and CI (Truthful Status)

### Automated checks currently implemented
- Python compile checks for all bot/API modules.
- Unit tests for `/ask` endpoint contract using mocked tutor calls.
- Python LOC policy check (`< 400` lines per file under `chris_tutor_bot/`).

### What is not yet automated
- End-to-end tests requiring live Ollama responses.
- Browser/UI integration tests for the dashboard.
- Deployment pipeline checks.

CI workflow: `.github/workflows/ci.yml`.
