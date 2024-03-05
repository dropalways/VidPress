@echo off
::del /f *.mkv
if "%~2" == "" (
  cmd
  exit
)
set crf=24
if not "%~3" == "" set crf=%~3
ffmpeg -i "%~1" -vcodec libx264 -c:a copy -crf %crf% "%~2"
