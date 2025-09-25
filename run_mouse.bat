:: Only the outputs of the program will be displayed
@echo off

:: Path to project
cd /d "C:\Users\egylk\Projects\moveMouse"

:: Activate the virtual environment
call .venv\Scripts\activate.bat

:: Run the script
python move_mouse.py