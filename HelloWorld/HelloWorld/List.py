#list demo
"""
shoplist=['apple','mango','carrot','banana']
print("I have",len(shoplist), "items to purchase.")

for item in shoplist:
    print(item)

shoplist.append("rice")

print(shoplist)

shoplist.sort()
print(shoplist)

olditem = shoplist[0]

del(shoplist[0])

print(shoplist)
"""

#元组 tuple
"""
zoo = ("wolf",'elephant','penguin')
print(zoo)

new_zoo=('monkey','dolphin',zoo)

print(new_zoo)

print(new_zoo[2])
print(new_zoo[2][2])
"""

#print tuple
"""
age=22
name='Swarppp'

print('%s is %d years old'%(name, age))

print('Why is %s playing with that python?'%name)
"""
#dictionary
"""
ab = {'Swarppp':'swaroopch@byteofpython.info','Larry' : 'larry@wall.org',
'Matsumoto' : 'matz@ruby-lang.org',
'Spammer' : 'spammer@hotmail.com'}
print("Swaroop's address is %s"%ab["Swarppp"])

ab['Guido'] = 'guido@python.org'

del ab['Spammer']

for name,address in ab.items():
    print("Contact %s at %s"%(name,address))

if('Guido' in ab):
    print("\nGuido's address is %s"%ab["Guido"])
"""


#sequence
"""
shoplist=['apple', 'mango', 'carrot', 'banana']
print("item 0 is",shoplist[0])
print("item 1 is",shoplist[1])
print("item 2 is",shoplist[2])
print("item 3 is",shoplist[3])
#print("item 4 is",shoplist[4])

print("item 1 to 3 is",shoplist[1:3])
print("item 2 to end is",shoplist[2:])
print("item 1 to -1 is",shoplist[1:-1])
print("item 1 to -2 is",shoplist[1:-2])
print("item start to end is",shoplist[:])

name='Swaroop'

print("characters 1 to 3 is ",name[1:3])
print("characters 2 to end is ",name[2:])
print("characters 1 to -1 is ",name[1:-1])
print("characters start to end is ",name[:])
"""

#reference
"""
print('Simple Assignment')

shoplist=['apple', 'mango', 'carrot', 'banana']

mylist=shoplist

del(shoplist[0])

print ("ShopList is ",shoplist)
print("MyList is ",mylist)

print("Copy by Make full slice")
mylist = shoplist[:]
del(mylist[0])

print ("ShopList is ",shoplist)
print("MyList is ",mylist)
"""

#str methods

name="Swaroop"

if name.startswith("Swa"):
    print("Yes ,its start with 'Swa'")

if 'a' in name:
    print("yes, name contains a string 'a'")

if name.find("war") != -1:
    print("yes, it contains the 'war'")

delimiter="_*_"
mylist = ['Brazil','Russia','India','China']
print(delimiter.join(mylist))

index = name.find("oop")

print(index)

