@echo off
rem D&D�����t�H���_�܂��̓t�@�C���̃p�X���X�N���v�g�ɓn��
cd /d %~dp0

echo D^&D���ꂽ�p�X ^> %1

set /p CMD="�X�N���v�g������͂��Ă������� >"
echo ^>%CMD% %1
%CMD% %1
pause