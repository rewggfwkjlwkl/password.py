@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not added to PATH.
    pause
    exit /b
)

REM Optionally, install dependencies
echo Installing required Python packages...
pip install boto3 botocore

REM Run the script
python aws_key_checker.py

pause
