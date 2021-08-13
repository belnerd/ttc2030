# Outputs
import time
import sys

# Print divider
def printDiv():
    for i in range(0,50):
        print('#',end='') 
    print('\n')

# Print given text in a delayed fashion, use sys.stdout because print(text,end='') functions incorrectly with time.sleep()
# ctrl+c to stop printing and return to main program
def printTextDelayed(text,delay):
    printDiv()
    try:
        for x in text + '\n':
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(delay)
    except KeyboardInterrupt:
        pass
    print('\n')
    printDiv()

# Print a "menu" based on the indexes of the file list
def printFileList(files):
    for x in files:
        index = str(files.index(x))
        print('['+index+'] '+x)

