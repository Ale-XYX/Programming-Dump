@echo off
set path=C:\Program Files\Java\jdk1.8.0_172\bin
set /p id="Enter File to compile: "
javac %id%
echo Done.
pause