# Weather Forecast API

A simple weather forecast API built with [FastAPI](https://fastapi.tiangolo.com/).

## Features

- `GET /weather/{city}` — Returns randomized weather data (condition, max temperature, min temperature) for any city.
- Example: `GET /weather/tokyo`

## Response Format

```json
{
  "city": "tokyo",
  "condition": "Sunny",
  "max_temp": 30,
  "min_temp": 10
}
```

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

### Install Dependencies

```bash
uv sync
```

### Run the Server

```bash
uv run uvicorn test20260827.main:app --reload
```

Then open http://127.0.0.1:8000/weather/tokyo in your browser.

### Run Tests

```bash
uv run pytest
```

## Project Structure

```
.
├── src/
│   └── test20260827/
│       ├── __init__.py
│       └── main.py       # FastAPI application
├── tests/
│   └── test_main.py      # pytest tests
├── pyproject.toml
└── README.md
```
