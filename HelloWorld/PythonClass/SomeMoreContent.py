
#list_comprehension
"""
listone=[2,3,4]

listtwo=[2*i for i in listone if i > 2]

print(listtwo)
"""
#pow sum
"""
def powersum(power, *args):
    total=0
    for i in args:
        total+= pow(i,power)
    return total

s = powersum(2,3,4)
print(s)

ss = powersum(2,10)
print(ss)
"""


#lambda
def make_repeater(n):
    return lambda s:s*n

twice=make_repeater(2)

print(twice("word"))

print(twice(5))

exec('print("Hello world")')

print(eval('2*3'))

mylist=['item']
assert len(mylist) >= 1
sitem = mylist.pop()

print(sitem)
