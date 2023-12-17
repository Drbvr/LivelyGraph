#!/bin/bash

echo "Creating a virtual environment..."
python -m venv strava-env

echo "Activating the virtual environment..."
source strava-env/bin/activate

echo "Installing required packages..."
pip install requests

echo "Environment setup complete."
