#!/bin/bash

set -euo pipefail

echo "Running tests with coverage"
uv sync
uv run pytest --cov --cov-report=html --cov-report=term --cov-report=term-missing
