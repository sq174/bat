import glob
import os
import sys
import string
import random
if len(sys.argv) > 1:   # カレントディレクトリの移動 
    if os.path.isfile(sys.argv[1]): #D&Dで渡されたファイル・フォルダのパスに移動する
        workplace = os.path.dirname(sys.argv[1])
    else:
        workplace = sys.argv[1]
else:
    workplace = sys.path[0] 	#デフォルトでは.pyファイルのある位置
os.chdir(workplace)
print("【Workplace】" + workplace)
files = glob.glob('*')

num = 0
for file in files:
    os.rename(file, "TMP" + str(num).zfill(3))
    num += 1

files = glob.glob('*')
num = 0
for file in files:
    os.rename(file, "FILE" + str(num).zfill(3) + ".mp4")
    print("【Rename】" + "FILE" + str(num).zfill(3) + ".mp4")
    num += 1
#input()

