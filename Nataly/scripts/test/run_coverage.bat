@echo off
setlocal ENABLEDELAYEDEXPANSION

rem Resolve project root relative to this script
set "SCRIPT_DIR=%~dp0"
pushd "%SCRIPT_DIR%\..\.."

set "VENV_PY=venv\Scripts\python.exe"
if not exist "%VENV_PY%" (
  echo [i] Virtualenv not found at venv\Scripts\python.exe
  echo [i] Create and activate venv, then install dev deps:
  echo     python -m venv venv
  echo     venv\Scripts\activate.bat
  echo     pip install -e .[dev]
  popd
  endlocal
  exit /b 1
)

echo Running pytest with coverage...
"%VENV_PY%" -m pytest --cov=src --cov-report=term-missing
set "EXIT_CODE=%ERRORLEVEL%"

popd
endlocal & exit /b %EXIT_CODE%

