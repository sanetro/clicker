@echo off

python --version 2>NUL
if not errorlevel 1 goto errorNoPython
if errorlevel 1 goto installModules


goto:eof

:errorNoPython
echo.
echo Error^: Python not installed

:installModules
pip install pygame
pip install sys
pip install os
pip install win32api