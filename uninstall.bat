@echo off
echo Uninstalling boto3 and botocore...

REM Check if Python is available
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH.
    pause
    exit /b
)

REM Uninstall the packages
pip uninstall -y boto3 botocore

echo Uninstallation complete.
pause
