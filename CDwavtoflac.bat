@echo off
cd /d %~dp0
for %%a in (%*) do python CDwavtoflac.py %%a
pause