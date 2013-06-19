@echo off
cd /d %~dp0
for %%a in (%*) do (
python CDrenamelog.py %%a
python CDwavtoflac.py %%a
python CDarrange.py %%a
)
pause