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

lamePath = "D:/Programs/lame-3.98.4/x64/lame.exe"
wavfiles = glob.glob('*.wav')   #wavファイルを取得

for wavfile in wavfiles:
    CDname = re.sub(".wav", '', wavfile)
    print("分割->mp3変換:" + CDname)
    mp3Path = "D:/Users/yk2/Music/" + re.sub("[\\\"<>:/|?* ]", '', CDname)
    if not os.path.isdir(mp3Path):
        os.mkdir(mp3Path)   #shntoolは特殊な文字を受け付けないようなので事前に変換している
    command = 'shntool split "' + CDname + '.wav" -f "' + CDname + '.cue" -o "cust ext=mp3 "D:/Programs/lame-3.98.4/x64/lame.exe" --preset insane - -o "' + mp3Path + '/%f"" -t "%n %t" '
    subprocess.check_call(command, shell=True)  #外部プログラムで変換を実行
#input()
