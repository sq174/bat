import sys
import os
import glob
import re
import zipfile
import subprocess
if len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1]):
        workplace = os.path.dirname(sys.argv[1])
    else:
        workplace = sys.argv[1]
else:
    workplace = sys.path[0]
os.chdir(workplace)

files = glob.glob('*.log')

for file in files:
    f = open(file)
    lines = f.read().split('\n')
    f.close()
    CDfilename = re.sub(" / ", " - ", lines[1], 1)
    print(CDfilename)
    os.rename(file, CDfilename + ".log")
    zipfiles = glob.glob(CDfilename + ".*")
    command = ["7z", "a", "-tzip", CDfilename + ".zip"] + zipfiles
    print(' '.join(command))
    subprocess.check_call(command, shell=True)
input()
