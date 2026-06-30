'''
Input Formatting
-----------------
-->Input means receiving data from the user while the program is running.
-->Python uses the input() function to accept user input.
-->By default, input() always returns data as a string
1.input()
---------
-->The input() function is used to take input from the user
i.int
-----
Ex:
num=89         //system input
num_2=int(input("Enter a number:"))  //User Input
print(num+num_2)

ii.string
----------
Ex:
hi=input("Enter a string:")
print(hi+" Hello")

iii.float
----------    
num=float(input("Enter a salary:"))  
print(num_2)

iv.list
--------
Ex:
grp=list(map(int,input().split()))  
print(grp)

grp=list(map(str,input().split()))  
print(grp)

grp=list(input().split())  
print(grp)

grp=list(input())  
print(grp)

v.tuple
--------
Ex.
grp=tuple(map(int,input().split()))  
print(grp)

grp=tuple(map(str,input().split()))  
print(grp)

grp=tuple(input().split())  
print(grp)

grp=tuple(input())  
print(grp)

vi.set
-------
EX:
numbers = set(map(int, input().split()))
print(numbers)

vii.dictionary
--------------
Ex:
keys = input().split()
values = map(int, input().split())

student = dict(zip(keys, values))
print(student)

Eval:
-----

--->This is simple form of input formatting of all data types
-->The eval() function automatically converts input into the appropriate Python data type.
Ex:
num=eval(input("enter:"))
print(type(num))

f:string or doc string format
-----------------------------
-->
Syntax:f"{}""{}
Ex:
name_=input("Enter your Name:")
age_=int(input("Enter your age:"))
print(name_,"your age is",age_)
print(f"{name_ } your age is {age_}")
print(f"{name_ } your age is {age_+6}")


Modules format
--------------
Ex:
name_=input("Enter your Name:")
age_=int(input("Enter your age:"))
print("my name is %s and i'm %d years old"%(name_,age_))

''' 

























