@echo off
:: Check for Python Installation
python --version 2>NUL
if not errorlevel 1 goto errorNoPython
pip install pygame
:: Reaching here means Python is installed.
:: Execute stuff...

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo.
echo Error^: Python not installed

