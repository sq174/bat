@echo off
rem 日付を取得
set YYYYMMDD=%DATE:/=%
rem バックアップ元ドライブ
set SD=S:\
rem バックアップ先の親フォルダ
set BACKUP=V:\3DSBackup\
rem バックアップの作成
robocopy %SD% %BACKUP%%YYYYMMDD% /e /log+:"%BACKUP%LOG\%YYYYMMDD%.log" /np /tee /fft /xf *.AVI
echo バックアップの完了
PAUSE
