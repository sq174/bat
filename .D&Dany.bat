@echo off
rem D&Dしたフォルダまたはファイルのパスをスクリプトに渡す
cd /d %~dp0

echo D^&Dされたパス ^>
for %%a in (%*) do echo %%a
echo.

set /p CMD="スクリプト名を入力してください >"
for %%a in (%*) do (
echo ^>%CMD% %%a
%CMD% %%a
)
pause