@echo off      
@set PATH=C:\SIMULIA\Commands\;%PATH%
@cd %cd%   
set str=0MakeStaticFreqCae.py
rem abaqus.bat cae noGUI=test.py 
rem abaqus.bat cae script=%str%
abaqus.bat cae noGUI=%str%

pause