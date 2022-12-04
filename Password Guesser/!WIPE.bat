@echo off
REM Copyright Disclaimer: 
REM Using this program normally falls under teaching
REM This content is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship and research. 
REM Fair use is a use permitted by copyright statute that might otherwise be infringing.
REM (Section 107 of the Copyright Act 1976)
echo [----] Only to be used in extreme situations, wipes all saved data!
echo [----] 10s until wipe, press anykey to skip
timeout 10 >NUL
echo [OKAY] Wiping...
python Wipe.py

pause