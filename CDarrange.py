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
    print("zip圧縮:" + CDfilename)
    print("zip圧縮:" + re.sub("[\[\]]", '?', CDfilename))
    zipfiles = glob.glob(re.sub("[\[\]]", '?', CDfilename) + '.*')
    complete = True
    if not CDfilename + ".cue" in zipfiles: #欠損があれば警告
        print("CAUSION:cueファイルが見つかりません")
        complete = False
    if not CDfilename + ".log" in zipfiles:
        print("CAUSION:logファイルが見つかりません")
        complete = False
    command = ["7z", "a", "-tzip", "W:/Contents/CD/" + CDfilename + ".zip"] + zipfiles
#    print(' '.join(command))
    subprocess.check_call(command, shell=True)
    if complete:    #欠損がなければzip元のファイルを削除する
        for zipfile in zipfiles:
            os.remove(zipfile)
        print("元のファイルを削除しました")
    else:
        print("元のファイルを残します")
existfiles = glob.glob('*.*')
if not existfiles:    #ディレクトリが空ならば，ディレクトリを削除
    os.chdir(sys.path[0])
    os.rmdir(workplace)
#input()
