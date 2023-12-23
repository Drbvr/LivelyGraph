#!/bin/bash

venv_name="strava-env"

echo "Creating virtual environment $venv_name"
python -m venv $venv_name
source $venv_name/bin/activate # on Windows use venv/\Scripts/activate

echo "Installing dependencies"
pip install Flask requests

echo "Setup complete. Use '.\n$venv_name/bin/activate' to activate the virtual environment"
