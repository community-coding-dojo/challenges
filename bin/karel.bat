@echo off
SET scriptpath=%~dp0

if not exist "%scriptpath%\..\venvs\karel" (
  python -m venv "%scriptpath%\..\venvs\karel"
)

"%scriptpath%\..\venvs\karel\Scripts\pip" install --upgrade -r "%scriptpath%\..\common\karel\requirements.txt"

"%scriptpath%\..\venvs\karel\Scripts\python" "%scriptpath%\..\common\karel\run.py"
