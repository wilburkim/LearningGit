
#sys template
"""
import sys

print ("the command line arguments are:")
for i in sys.argv:
    print (i)

print("\n\n The PythonPath is ",sys.path,'\n')
"""

#module name
"""
if __name__ == '__main__':
    print ("the programe is being run by itself")
else:
    print("i am being imported from another module")
"""

#using my module
"""
import Mymodule
Mymodule.sayHi()

print ("Version:",Mymodule.Version)
"""
