'''
polymorphism
-------------
-->Ploymorphism means many forms
-->It allows same method, function or operator to perform different tasks depending on the same object...

types
-----
1.Method overloading
---------------------
--> Means having multiple methods with the same name but different parameters
eg:
class Cal:
    def add(self,num,num_2=0):
        print(num+num_2)
obj = Cal()
obj.add(4,7)

eg:
class Cal:
    def add(self,num,num_2=0):
        print(num+num_2)
    def add(self,num,num_2=0,num_3=0):
        print(num+num_2+num_3)
obj = Cal()
obj.add(4,7,9)

eg:
class Cal:
    def add(self,num,num_2=0):
        print(num+num_2)
    def add(self,num,num_2=0,num_3=0):
        print(num+num_2+num_3)
obj = Cal()
obj.add(4,7)
obj.add(3,57)

eg:
class Cal:
    def add(self,num,num_2=0):
        print(num+num_2)
    def add(self,num,num_2=0,num_3=7):
        print(num+num_2+num_3)
obj = Cal()
obj.add(3,57)

2.method overriding(two different class but same method)
--------------------------------------------------------
-->The method overriding occurs when a child class provides its own implementation of a method already defined in its parent class...

eg:
class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def sound(self):
        print("Dogs barks")
d = dog()
d.sound()

3.Operator overloading
-----------------------
-->This allows operators (+,-,*) to work differently for user-defined objects
1.__add__
2.__sub__
3.__mul__
4.__truediv__(/)
5.__eq__() (==)
6.__It__() (<)

1.__add__
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
s1 = student(56)
s2 = student(67)
print(s1 + s2)

2.__sub__
class student:
    def __init__(self,marks):
        self.marks = marks
    def __sub__(self,other):
        return self.marks * other.marks
s1 = student(56)
s2 = student(67)
print(s1 - s2)

3.__mul__
class student:
    def __init__(self,marks):
        self.marks = marks
    def __mul__(self,other):
        return self.marks * other.marks
s1 = student(56)
s2 = student(67)
print(s1 * s2)

Data abstraction
-----------------
-->Data abstraction is the process of hiding implementation details and showing only essential datato the user
eg:
->ATM
->Car
->App

eg:
from abc import ABC, abstractmethod
class bank:
    @abstractmethod
    def intrest(self):
        raise NOTImplementedError('Subclass must implemented intrest()')
class SBI(bank):
    def intrest(self):
        print('SBI intrest Rate: 6.5%')
class HDFC(bank):
    def intrest(self):
        print('HDFC intrest Rate: 5.5%')
class ICIC(bank):
    def intrest(self):
        print('ICIC intrest Rate: 6.9%')
banks = [SBI(),HDFC(),ICIC()]

for j in banks:
    j.intrest()

'''





















