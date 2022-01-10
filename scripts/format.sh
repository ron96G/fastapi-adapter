#!/usr/bin/env bash
set -e

poetry run black fastapi_adapter tests
poetry run isort fastapi_adapter tests