# Reminder to set the .sh as executable first:
# chmod +x setup.sh
# ./setup.sh


#!/bin/bash

# Step 1: Create virtual environment
python3 -m venv venv

# Step 2: Activate virtual environment
source venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

echo "Virtual environment created, activated, and dependencies installed."
