
#if and else if
"""
number = 23
guess = int(input("Enter an interger:"))

if guess == number:
    print("Congratulation, u guess it.")
    print("But u do not win any prizes!")
elif guess < number:
    print("No its a little higher ")
else:
    print("No , its a little lower")

print("Done")

"""


#while loop
"""
number = 23
running = True;
while running:
    guess = int(input('Enter an integer:'))
    if guess == number:
        print("Congratulation, u guessed it")
        running = not running;
    elif guess < number:
        print("No, its a little higer")
    else:
        print("No ,its a little lower")
#else:
print ("the while loop is over");
print("Done");
"""

#for loop
"""
for i in range(1,5):
    print ("the result is",i)
print ("the for loop is done")
"""

#while break loop
"""
while True:
    s = input("Enter something:")
    if s=="quit":
        break
    print ("Length of the string is",len(s))
print ("Done");
"""

#while break and continue loop
while True:
    s = input("Enter something:")
    if s=="quit":
        break
    if len(s) < 3:
        continue
    print ("Length of the string is",len(s))
print ("Done");