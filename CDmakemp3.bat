@echo off
cd /d %~dp0
for %%a in (%*) do python CDmakemp3.py %%a
pause