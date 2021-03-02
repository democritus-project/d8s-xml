#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_xml/ tests/

black democritus_xml/ tests/

mypy democritus_xml/ tests/

pylint --fail-under 9 democritus_xml/*.py

flake8 democritus_xml/ tests/

bandit -r democritus_xml/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_xml/ tests/
