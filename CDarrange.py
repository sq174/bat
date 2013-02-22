import sys
import os
import glob 
if len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1]):
        workplace = os.path.dirname(sys.argv[1])
    else:
        workplace = sys.argv[1]
else:
    workplace = '.'
os.chdir(workplace)

files = glob.glob('*.log')

for file in files:
    print(file)
input()
