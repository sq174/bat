@echo off
cd /d %~dp0
for %%a in (%*) do python renameDUMMY.py %%a
pause