import glob
import os
import string
import random

os.chdir("D:/temp/DUMMY_FILES")

files = glob.glob('*')

num = 0
for file in files:
    os.rename(file, "TMP" + str(num).zfill(3))
    num += 1

files = glob.glob('*')
num = 0
for file in files:
    os.rename(file, "FILE" + str(num).zfill(3) + ".mp4")
    num += 1
#input()

