import sys
import os
import glob
import re
import zipfile
import subprocess
if len(sys.argv) > 1:   	#カレントディレクトリの移動
    if os.path.isfile(sys.argv[1]):
        workplace = os.path.dirname(sys.argv[1])
    else:
        workplace = sys.argv[1]
else:
    workplace = sys.path[0] #デフォルトでは.pyファイルの場所
os.chdir(workplace)

wavfiles = glob.glob('*.wav')   #wavファイルを取得

for wavfile in wavfiles:
    CDname = re.sub(".wav", '', wavfile)
    print(CDname)
    command = ["flac", CDname + ".wav" ]
    subprocess.check_call(command, shell=True)  #外部プログラムで圧縮を実行
    os.remove(CDname + ".wav")
    if os.path.exists(CDname + ".cue"):  #cueファイルの書き換え .wav -> .flac
        cuefile = open(CDname + ".cue", 'r')
        lines = cuefile.readlines()
        cuefile.close()
        lines[4] = re.sub(".wav", ".flac", lines[4], 1)
        cuefile = open(CDname + ".cue", 'w')
        cuefile.writelines(lines)
        cuefile.close()
    else:
        print("cueファイルが存在しません")
#input()
