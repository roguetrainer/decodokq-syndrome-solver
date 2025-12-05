@echo off
REM Setup script for Decodok-Q: Quantum Error Correction Games (Windows)
REM This script creates a virtual environment and installs all dependencies

setlocal enabledelayedexpansion

echo ================================================================
echo      Decodok-Q: Quantum Error Correction Games Setup
echo ================================================================
echo.

REM Check if Python is installed
echo [*] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Found Python %PYTHON_VERSION%
echo.

REM Check if virtual environment already exists
if exist venv (
    echo [*] Virtual environment already exists. Removing old one...
    rmdir /s /q venv
)

REM Create virtual environment
echo [*] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment created
echo.

REM Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment activated
echo.

REM Upgrade pip
echo [*] Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1
echo [OK] pip upgraded
echo.

REM Install requirements
echo [*] Installing dependencies from requirements.txt...
if not exist requirements.txt (
    echo [ERROR] requirements.txt not found!
    pause
    exit /b 1
)

pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed
echo.

REM Verify installations
echo [*] Verifying installations...

python -c "import numpy" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] NumPy not installed correctly
) else (
    for /f %%i in ('python -c "import numpy; print(numpy.__version__)"') do set NUMPY_VERSION=%%i
    echo   [OK] NumPy !NUMPY_VERSION!
)

python -c "import pytest" >nul 2>&1
if errorlevel 1 (
    echo   [WARNING] pytest not found (optional)
) else (
    for /f %%i in ('python -c "import pytest; print(pytest.__version__)"') do set PYTEST_VERSION=%%i
    echo   [OK] pytest !PYTEST_VERSION!
)

where jupyter >nul 2>&1
if errorlevel 1 (
    echo   [WARNING] Jupyter not found (recommended for notebooks)
) else (
    echo   [OK] Jupyter installed
)

echo.

REM Test imports
echo [*] Testing game imports...
python -c "from src.codes import SteaneCode, SteaneGame, ReedMullerCode, ReedMullerGame" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Failed to import game modules
    echo This might be okay if setting up for the first time
) else (
    echo [OK] Game modules imported successfully
)

echo.

REM Create activation helper script
echo [*] Creating activation helper script...
(
echo @echo off
echo call venv\Scripts\activate.bat
echo echo Virtual environment activated!
echo echo To deactivate, run: deactivate
) > activate_env.bat
echo [OK] Created activate_env.bat
echo.

REM Summary
echo ================================================================
echo                   Setup Complete! 🎉
echo ================================================================
echo.
echo Next steps:
echo.
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo    (or use: activate_env.bat)
echo.
echo 2. Try a quick demo:
echo    python examples\simple_steane_demo.py
echo.
echo 3. Or start Jupyter for interactive learning:
echo    jupyter notebook examples\steane_game_demo.ipynb
echo.
echo 4. Read the documentation:
echo    • GAMES-README.md (start here)
echo    • docs\games\QUICK-START-GUIDE.md
echo.
echo Troubleshooting:
echo • If imports fail, make sure you're in the project root directory
echo • For Jupyter issues: pip install jupyter
echo • To deactivate the environment: deactivate
echo.
echo Happy quantum error correcting! ⚛️
echo.

pause
