@echo off
cd /d %~dp0
for %%a in (%*) do python CDrenamelog.py %%a