# python-template

Production-ready Python template for building well-tested, layered applications.

## Stack

- Python 3.12+
- Pytest + coverage
- Ruff + mypy
- uv (package manager)

## Commands

- `make install` — install production dependencies
- `make install-dev` — install dev dependencies
- `make run` — run the application
- `make test` — run tests with coverage
- `make docker-build` — build Docker image
- `make docker-test` — run tests in Docker

## Project Structure

```text
.
├── main.py
├── app/
│   ├── domain/         # domain models
│   ├── repositories/   # data-access abstractions
│   └── services/       # business logic
└── tests/
    ├── unit/
    └── e2e/
```

## Architecture

- `app/services`: business logic
- `app/repositories`: data-access abstractions
- `app/domain`: domain models
- `tests`: unit and integration suites

## Quality Gates

- Lint must pass.
- Typecheck must pass.
- Test suite must pass.
- Coverage report generated on test runs.
