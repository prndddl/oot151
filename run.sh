#!/bin/sh

# Create a virtual environment
py -m venv venv

# Activate the virtual environment
. venv/Scripts/activate

# Install dependencies
py -m pip install requests pyyaml

# Run scripts
py ./src/generate_csv.py
py ./src/generate_yamls.py