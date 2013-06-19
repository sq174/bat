@echo off
rem D&Dしたフォルダまたはファイルのパスをスクリプトに渡す
cd /d %~dp0

echo D^&Dされたパス ^> %1

set /p CMD="スクリプト名を入力してください >"
echo ^>%CMD% %1
%CMD% %1
pause