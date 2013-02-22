@echo off
cd /d %~dp0
for %%a in (%*) do python CDarrange.py %%a
pause