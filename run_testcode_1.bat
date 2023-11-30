@echo off
:loop
python testcode_1.py

echo.
echo Press "Ctrl+C" to stop the loop.
timeout /t 10 /nobreak >nul
goto loop