'''
Self Keyword
-------------
-->Self refers to current object...
ex:
class Test:
    def display(self):
        print(self)
t=Test()
print(t)
t.display()



Constructor
------------
-->This constructor initialize the object automatically
when it is created 

ex:
class Batch:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def display(self):
        print(self.name)
        print(self.branch)
b4=Batch('likki','csd')
b4.display()


Access Specifiers
------------------
1.Public variable
----------------
EX:
class Batch:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def display(self):
        print(self.name)
        print(self.branch)
b4=Batch('likki','csd')
b4.display()

2.Protected variable
-------------------
ex:
class Batch:
    def __init__(self,name,branch):
        self._name=name
        self.branch=branch
    def display(self):
        print(self._name)
        print(self.branch)
b4=Batch('likki','csd')
b4.display()

EX2:
class fam:
    def __init__(self,name):
        self._name=name
f=fam()
print(f._name)

Private variable
-----------------
Ex:Outside the class access the variable 
class bank:
    def __init__(self):
        self.__pin='0987'
AC=bank()
print(AC._bank__pin)

Ex2:Inside the class access the variable 
class bank:
    def __init__(self):
        self.__pin='0987'
    def display(self):
        print(self.__pin)
AC=bank()
AC.display()


Encapsulation
--------------
-->It means wrapping the data and methods into a single unit(class)
while controlling access to the data

Ex:
class Atm:
    def __init__(self,balance):
        self._balance=balance
    def deposite(self,amount):
        self._balance+=amount
        print(self._balance)
tran=Atm(7000)
tran.deposite(300)

'''




















    
