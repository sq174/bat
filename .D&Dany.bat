@echo off
rem D&D�����t�H���_�܂��̓t�@�C���̃p�X���X�N���v�g�ɓn��
cd /d %~dp0

echo D^&D���ꂽ�p�X ^>
for %%a in (%*) do echo %%a
echo.

set /p CMD="�X�N���v�g������͂��Ă������� >"
for %%a in (%*) do (
echo ^>%CMD% %%a
%CMD% %%a
)
pause