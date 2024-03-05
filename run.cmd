@echo off
if "%~1" == "" (
  echo Drag a file onto this script to compress it.
  pause
  exit
)
python main.py "%~1" "compressed_%~n1.mp4"

pause