
#excepiton input
"""
import sys
try:
    s = input("enter somtion")

except EOFError:
    print("\n why did u do an eof on me?")
    sys.exit()

except exx:
    print("\n Some error /exception occurred", exx )

print("done")
"""

# raise exception
"""
class ShortInputException(Exception):
    def __init__(self,length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleaset=atleast

try:
    s = input("enter something")

    if(len(s) < 5):
        raise ShortInputException(len(s),5)
except EOFError:
    print("\n why did u do an eof on me?")

except ShortInputException as x:
    print("ShortInputException:the input was of length %d,at least %d"%(x.length,x.atleaset))
else:
    print("No Exception raised")
"""

#try and finally
import time
try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line)
finally:
    f.close()
    print("Cleaning up...closed the file")