
#sayHello
"""
def sayHello():
    print("Hello world")


sayHello();
"""

#print Max
"""
def printMax(a,b):
    if(a > b):
        print(a,"is maximum")
    else:
        print(b,"is maximum")

printMax(5,6)

printMax('a','b')

printMax('z','a')
"""

#inner parameter
"""
def func(x):
    print ("X is ",x)
    x = 5
    print("the change result x is",x)

x = 50
func(x)

print("the final x is",x)
"""

#global parameter
"""
def func():
    global x
    print ("x is ",x)
    x = 2;
    print ("the changed x is ",x)

x=50
func()

print ("the final x is ",x)
"""

#defalut value parameter
"""
def saySomething(message, times = 1):
    print (message * times)

saySomething('Hello')
saySomething("World",5)
"""

#key parameter
"""
def func(a,b=5,c=10):
    print("a is",a,"b is ",b,"c is",c)

func(3,7)
func(25,c=24)
func(c=50,a=100)
"""

#return value
"""
def maximum(x,y):
    if(x>y):
        return x
    else:
        return y

print(maximum(5,55))
print(maximum('a','z'))
"""

#dosomething
def printMax(x,y):
    """Prints the maximum of two numbers.
    the twon values must be integers."""
    x = int(x)
    y = int(y)
    if(x > y):
        print(x,"is maximum")
    else:
        print(y,"is maximum")


printMax(5,100)
printMax(5.1,5.9)
print(printMax.__doc__)