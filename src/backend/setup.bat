@echo off

REM Step 1: Create virtual environment
python -m venv venv

REM Step 2: Activate virtual environment
call venv\Scripts\activate

REM Step 3: Install dependencies
pip install -r requirements.txt

echo Virtual environment created, activated, and dependencies installed.
