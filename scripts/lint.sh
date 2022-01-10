#!/usr/bin/env bash

set -e

poetry run black --check fastapi_adapter tests
poetry run isort --check-only fastapi_adapter tests
poetry run mypy fastapi_adapter