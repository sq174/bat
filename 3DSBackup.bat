@echo off
rem ���t���擾
set YYYYMMDD=%DATE:/=%
rem �o�b�N�A�b�v���h���C�u
set SD=S:\
rem �o�b�N�A�b�v��̐e�t�H���_
set BACKUP=V:\3DSBackup\
rem �o�b�N�A�b�v�̍쐬
robocopy %SD% %BACKUP%%YYYYMMDD% /e /log+:"%BACKUP%LOG\%YYYYMMDD%.log" /np /tee /fft /xf *.AVI
echo �o�b�N�A�b�v�̊���
PAUSE
