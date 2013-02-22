import sys
import os
import glob
import re
import zipfile
import subprocess
if len(sys.argv) > 1:   # カレントディレクトリの移動 
    if os.path.isfile(sys.argv[1]): #D&Dで渡されたファイル・フォルダのパスに移動する
        workplace = os.path.dirname(sys.argv[1])
    else:
        workplace = sys.argv[1]
else:
    workplace = sys.path[0] 	#デフォルトでは.pyファイルのある位置
os.chdir(workplace)

files = glob.glob('*.flac')

for file in files:  	#.flacファイルを取得し、.cue .logファイルをまとめてzipに圧縮
    CDfilename = re.sub(".flac", '', file)
    print("圧縮:" + CDfilename)
    zipfiles = glob.glob(CDfilename + ".*")
    complete = True
    if not CDfilename + ".cue" in zipfiles: #欠損があれば警告
        print("cueファイルが存在しません")
        complete = False
    if not CDfilename + ".log" in zipfiles:
        print("logファイルが存在しません")
        complete = False
    command = ["7z", "a", "-tzip", "W:/Contents/CD/" + CDfilename + ".zip"] + zipfiles
#    print(' '.join(command))
    subprocess.check_call(command, shell=True)
    if complete:    #欠損がなければzip元のファイルを削除する
        for zipfile in zipfiles:
            os.remove(zipfile)         

input()
