import os
import sys
import glob
import subprocess
if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        dummynum = int(sys.argv[1])
    else:
        print("引数に数字を指定してください")
        input()
        exit
else:
    print("引数がありません")
    input()
    exit
os.chdir(sys.path[0])
sourcefile = "dat/DUMMY_FILES.zip"

folders = glob.glob("W:/FILES/*")
pivot = len(folders)
for i in range(0, dummynum):
    command = ["7z", "e", sourcefile, "-oW:/FILES/FILES" + str(pivot).zfill(3)]

    subprocess.check_call(command, shell=True)
    pivot += 1
input()
