import os
import shutil
import time

days = 30 
myPath = input('Enter the File Path: ')

def main():
    currentSeconds = time.time() - (days*24)
    if os.path.exists(myPath):
        for i,j,k in os.walk(myPath):
            if currentSeconds >= os.stat(i).st_ctime:
                removeFolder(i)
                break
            else:
                print('Folder Not Old Enough')
                for folder in j:
                    folderPath = os.path.join(i,folder)
                    if currentSeconds >= os.stat(folderPath).st_ctime:
                        removeFolder(folderPath)
                for file in k:
                    filePath = os.path.join(i,file)
                    if currentSeconds >= os.stat(filePath).st_ctime:
                        removeFile(filePath)
    else:
        print('Path is not Found')


def removeFolder(root):
    if not shutil.rmtree(root):
        print('Folder Removed Succesfully')
    else:
        print('Unable To Delete')

def removeFile(root):
    if not os.remove(root):
        print('File Removed Succesfully')
    else:
        print('Unable To Delete')

main()

