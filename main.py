import os

print os.name

PATH = os.getcwd()
print  PATH

FILES = os.listdir(PATH)
print  FILES

DIR = 'D:\ptest'
NEWFILES = os.listdir(DIR)
print  NEWFILES

for files in NEWFILES:
    print files
