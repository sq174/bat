import glob 

files = glob.glob('*.log')

for file in files:
    print(file)
input()
