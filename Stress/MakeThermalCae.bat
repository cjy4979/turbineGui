@ echo off
@ set PATH=C:/SIMULIA/Commands/;%PATH%
@ cd %cd% 
rem abaqus.bat cae noGUI=test.py
rem abaqus.bat cae script=C:/Users/CJY/Desktop/GUI0724/smt/dist/GUI_0724/0MakeThermalCae.py
abaqus.bat cae noGUI=C:/Users/CJY/Desktop/GUI0724/smt/dist/GUI_0724/0MakeThermalCae.py

pause