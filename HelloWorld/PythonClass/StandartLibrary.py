#sys library
"""
import sys
def readFile(filename):
    f=open(filename)
    while True:
        line = f.readline()
        if(len(line) == 0):
            break
        print(line)
    f.close()

if len(sys.argv) < 2:
    print("No action specified.")
    sys.exit()

if sys.argv[1].startswith('--'):
    option=sys.argv[1][2:]
    if option == 'version':
        print("Version 1.2")

    elif option == 'help':
        print("this help")

    else:
        print ("Unknown option.")

    sys.exit()

else:
    for fileName in sys.argv[1:]:
        readFile(filename)
"""


#os library
import os
print(os.name)
print(os.getcwd())
print(os.listdir())
print(os.linesep)
print(os.path.split("/"))