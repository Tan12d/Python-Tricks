import os

PATH = 'C:/Users/User/Desktop/All files/COLLEGE/4TH YEAR/8TH SEMESTER/Senior Design Project'

fileCount = 0
dirCount = 0

for root, dirs, files in os.walk(PATH):
    print('Loooking in: ',root)
    for directories in dirs:
        print(directories)
        dirCount+=1
    for Files in files:
        # print(Files)
        fileCount+=1
    
print('Number of files', fileCount)
print('Number of Directories', dirCount)
print('Total: ',(dirCount+fileCount))