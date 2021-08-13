# File operations
import os # For directory listing


# List compatible files at target directory, return as list
def listFiles(path,ext):
    fileList = list()
    try:
        for x in os.listdir(path):
            if x.endswith(ext):
                fileList.append(x)
        if len(fileList) > 0:
            return fileList
        else:
            print('Folder has no compatible files!')
            return False # Returns false if no compatible files found in directory
    except Exception as err:
        print('Error getting directory listing:'+err)

# Read file contents and return as a string, encoding presumed to be utf-8
def readFile(path,filename):
    try:
        file = open(path+filename,'r',encoding='utf-8')
        text = file.read()
        file.close()
        if len(text) > 0:
            return text
        else:
            print ('File is empty!')
            return False
    except Exception as err:
        print('Error reading file:'+err)

# Write text to end of target file at path
def writeFile(path, filename, text):
    try:
        file = open(path+filename,'a', encoding='utf-8')
        file.write(text)
        file.close()
    except Exception as err:
        print('Error writing to file:'+err)