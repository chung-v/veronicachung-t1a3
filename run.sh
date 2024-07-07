#!/bin/bash

# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "Python 3 is installed."

# Create a virtual environment if it does not exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install the dependencies from requirements.txt
pip install -r requirements.txt

# Change directory to src that contains the application
cd src

# Run the main application
python3 main.py

# Deactivate the virtual environment
deactivate