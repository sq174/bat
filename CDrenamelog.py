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
    os.rename(file, re.sub("[\\\"<>:/|?*]", ' ', CDfilename) + ".log")
    print("LOGファイル名変更:" + CDfilename)
#input()
