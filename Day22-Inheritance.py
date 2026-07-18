'''
Inheritance
-------------
-->Inheritance is an OOP concept where one class(child/derived)acquried the properties
and methods of another class(parent/base)

Ex:
class parent:
    pass
class child(parent):
    pass

1.Single Inheritance
---------------------
-->A child class inherits from one parent is Single Inheritance

EX:
class animals:
    def sound(self):
        print("Animals name sounds")
class dog(animals):
    def bark(self):
        print("Dog barks")
d=dog()
d.sound()
d.bark()

Ex2:
class father:
    def land(self):
        print("5 acres of land")
class son(father):
    def flat(self):
        print("3BHK flat")
s=son()
s.land()
s.flat()

2.Multiple Inheritance
-----------------------
-->A child class inherit more than one parent class is called multiple inheritance

Ex:
class father:
    def skills(self):
        print("Driving")
class mother():
    def talent(self):
        print("cooking")
class sister:
    def learn(self):
        print("fighting")
class son(father,mother,sister):
    def mine(self):
        print("coding")
all_=son()
all_.skills()
all_.talent()
all_.learn()
all_.mine()

3.Multilevel Inheritance:
-------------------------
-->One child class becomes the parent for another Class

Ex:
class grandfather:
    def house(self):
        print("Owns HOuse")
class father(grandfather):
    def flat(self):
        print("New flat")
class son(father):
    def own(self):
        print("have a car")
fam=son()
fam.house()
fam.flat()
fam.own()

4.Hierarical Inhertance
------------------------
-->Multiple childs inherit from the same parent

Ex:
class mother:
    def gold(self):
        print(" 10 kg gold")
class pinky(mother):
    def show(self):
        print("will get 5 kg gold")
class yuktha(mother):
    def shows(self):
        print("will get remaining 5 kg gold")
p=pinky()
y=yuktha()

p.gold()
p.show()

y.gold()
y.shows()
        
Ex:
class father:
    def land(self):
        print(" 6 acrs land")
class son1(father):
    def show(self):
        print("Will get 2 acrs")
class son2(father):
    def show_2(self):
        print("Will get 2 acrs")
class son3(father):
    def show_3(self):
        print("Will get 2 acrs")
        
s1=son1()
s2=son2()
s3=son3()

s1.land()
s1.show()

s2.land()
s2.show_2()

s3.land()
s3.show_3()

5.Hybrid Inhertance:
--------------------
-->This is the cobination of 2 or more types of inhertance

EX:example of multiple and multilevel
class A:
    def methodA(self):
        print("Class A")
class B(A):
    def methodB(self):
        print("Class B")
class C(A):
    def methodC(self):
        print("Class C")
class D(B,C):
    def methodD(self):
        print("Class D")
so=D()
so.methodA()
so.methodB()
so.methodC()
so.methodD()

Super():
--------
-->this super() function used to access parent class methods or constructors
in the child class

Ex:Methods
class parent:
    def show(self):
        print("This is the parent method")
class child(parent):
    def show(self):
        super().show()
        print("This is child class")
c=child()
c.show()

Ex2:Constructors
class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,rollno):
        super().__init__(name)
        self.rollno=rollno
    def display(self):
        print(self.name)
        print(self.rollno)
a=student("likki",101)
a.display()

'''




















