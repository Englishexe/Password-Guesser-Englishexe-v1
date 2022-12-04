@echo off
REM Copyright Disclaimer: 
REM Using this program normally falls under teaching
REM This content is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship and research. 
REM Fair use is a use permitted by copyright statute that might otherwise be infringing.
REM (Section 107 of the Copyright Act 1976)
echo [OKAY] Started batch
echo [INFO] Batch will be plain white and python multi-color
title Password Guesser  Englishexe  v1
echo [OKAY] Started title
echo [OKAY] Checking System, If this fails reinstall the program from 'link'
python Check.py
echo [OKAY] Starting python
for /f "Delims=" %%a in (Arguments.txt) do (
set Arguments=%%a
)
python App.py %Arguments%
echo [WARN] App crashed, press X to close
echo [INFO] Attempting Repair...
timeout 1 >NUL
python Check.py
pause >NUL