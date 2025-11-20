@echo off
setlocal ENABLEDELAYEDEXPANSION

if not exist "..\..\venv\Scripts\activate.bat" (
  echo [i] Activate your virtualenv before running tests: venv\Scripts\activate.bat
) else (
  call ..\..\venv\Scripts\activate.bat
)

echo Running pytest...
python -m pytest -q

endlocal


