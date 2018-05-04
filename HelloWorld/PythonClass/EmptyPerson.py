
#empty person class
"""
class Person:
    pass

p = Person()

print (p)
"""

#one function person class
""" 
class Person:
    def sayHi(self):
        print("Hello,how are u?")


p = Person()
p.sayHi()
Person().sayHi();
"""

#__init__ function person class
"""
class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("Hello,myname is",self.name)

p = Person('Swaroop')

p.sayHi()
"""

#class and class's object
"""
class Person:
    population = 0

    def __init__(self,name):
        self.name=name
        print("Initializing %s"%self.name)
        Person.population += 1

    def __del__(self):
        print("%s says bye"%self.name)
        Person.population -= 1
        if Person.population == 0:
            print("I am the last one")
        else:
            print("there are still %d people left."%Person.population)

    def sayHi(selft):
        print("Hi,my name is %s"%selft.name)
    
    def howMany(self):
        if(Person.population == 1):
            print("I am the only person here")

        else:
            print("We have %d persons here."%Person.population)


swaroop = Person("Swaroop")
swaroop.sayHi()
swaroop.howMany()

kalam = Person("Kalam")
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()

del(kalam)

del(swaroop)

"""

#类的继承
class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Initialized schoolmember:%s"%self.name)

    def tell(self):
        print("Name:%s Age:%d"%(self.name,self.age))

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print("Initialized Teacher:%s"%self.name)

    def tell(self):
        SchoolMember.tell(self)
        print("Salary:%d"%self.salary)

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print("Initialized Teacher:%s"%self.name)

    def tell(self):
        SchoolMember.tell(self)
        print("Marks:%d"%self.marks)


t = Teacher("Mrs.Shrividya",40,30000)
s = Student("Swaroop",22,75)

print()

members=[t,s]
for member in members:
    member.tell()