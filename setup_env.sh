#!/bin/bash

venv_name="strava-env"

echo "Creating virtual environment $venv_name"
python -m venv $venv_name
source $venv_name/bin/activate # on Windows use venv/\Scripts/activate

echo "Installing dependencies"
pip install -r requirements.txt

echo "Setup complete. Use '.$venv_name/bin/activate' to activate the virtual environment"
