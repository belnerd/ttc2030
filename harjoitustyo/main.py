# Main program

# Import functions from built-in libraries and external files
# os imported for directory functions
# sys for command line arguments
# datetime for date and functions
# fileops for file handling functions
# outputs for printing items

import os
import datetime
import sys
from fileops import * 
from outputs import *

# Global variables
ext = ".txt" # Compatible files extension
folder = "\\texts\\" # subfolder for the texts
path = os.getcwd()+folder
filesList = listFiles(path,ext)

# output delay per character in seconds from cli argument
if (len(sys.argv) > 0):
    try:
        delay = float(sys.argv[1])
    except Exception as err:
        delay = 0
        pass

# Menu for choosing the file to print
def menu():
    printDiv()
    filesList = listFiles(path,ext)
    print('Hakemiston '+path+' yhteensopivat tiedostot:')
    printFileList(filesList)
    start = 0
    stop = len(filesList)-1
    if (start is not stop):
        choice = input('Valitse tiedosto ['+str(start)+'-'+str(stop)+'] (exit lopettaaksesi): ')
    else:
        choice = input('Valitse tiedosto ['+str(start)+'] (exit lopettaaksesi): ')
    if (choice != 'exit' and choice != 'EXIT'):
        try:
            numchoice = int(choice)
            if (numchoice >= start and numchoice <= stop): #Check if choice is within range
                return numchoice
            elif (numchoice <= 0 or numchoice > stop):
                raise Exception
        except Exception as err:
            print('Virheellinen valinta!')
            menu()
    else:
        print('Heippa!')
        quit()

# Write something (a log entry) to the read file 
def writeLog(path,filename):
    print('Haluatko jättää lokimerkinnän tiedostoon (ENTER skippaa)?')
    nick = input('Nimimerkkisi: ')
    if (nick != ''):
        date = datetime.datetime.now()
        log = input('Lokimerkintäsi:')
        # Format the text for log
        log = '\n'+'>>'+date.strftime("%d.%m.%Y klo %H.%M")+' '+nick+' kirjoitti: '+log 
        try:
            writeFile(path,filename,log)
            print('Kirjoitettiin lokimerkintä!')
        except Exception as err:
            print('Virhe: '+err)


# Main program loop
while True:
    txtIndex = menu()
    try:
        text = readFile(path,filesList[txtIndex])
        if (text is not False):
            printTextDelayed(text,delay)
            writeLog(path,filesList[txtIndex])
        else:
            continue
    except Exception as err:
        print('Virhe: '+str(err))
        continue
