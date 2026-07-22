@echo off

echo Installing dependencies...

python -m pip install -r requirements.txt
python -m pip install pyinstaller


echo Building MoodMate AI EXE...

python -m PyInstaller ^
--clean ^
--windowed ^
--name MoodMateAI ^
--paths app ^
app/main.py


echo.
echo Build finished!
echo Check the dist folder.

pause