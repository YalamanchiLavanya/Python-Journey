'''
Functions
-----------
-->Functions is a block of code that can be reusable
-->Functions can be avoid the repeated lines of code

Functions of 2 Types
---------------------
1.Built-in Functions
---------------------
Ex:
1.print()
2.max()
3.type()
4.min()
5.len()
6.sum().........

2.User-define
--------------
-->This functions starts with the keyword "def()"
Syntax:
def func_name(parameters):   #Definition line
    -------------------
    --------------------
func_name(arguments)         #calling line

Ex:
def add():
    print("hello")
add()     

Types of Arguments
-------------------
-->we have types of arguments
1.Required Arguments
--------------------
-->we have to pass same number of arguments with definition of the function
Syntax:
def func(p1,p2):
    -----------
    -----------
func(a1,a2)

EX1:
def add(a,b):
    print(a+b)
add(2,6)
Ex2:
def add(a,b):
    print(a+b)    #it gives an error
add(2)

Ex3:
def add(a,b):
    print(a+b)   #it also gives  error
add(2,6.8)


2.Default Arguments
-------------------
-->
Syntax:
EX;
def add(a,b):
    print(a+b)
add(b=8,a=70)

EX2:
num=3
num_2=9
num_3=7
def add(a,b,c):
    print(a)
    print(b)
    print(c)
add(num,num_2,num_3)    

3.keyword Arguments
--------------------
-->We can pass as a pair like (variable=datatype/value)
Syntax:
def func(p1,p2):
    -----------
    -----------
func(p1=a1,p2=a2)

EX:
def add(a,b):
    print(a+b)
add(a=2,b=6)    

EX2:
def add(a,b):
    print(a)
add(a='b',b='c')

4.variable length Arguments
----------------------------
-->Can pass n number of arguments and just  use  (*args) in the parameter,will receive Tuple of arguments
-->Can pass n number of arguments and just  use  (**args) in the parameter,will receive Dictionary of arguments
SyntaX:
1.def func(*p):
   --------
  func(a1,a2,a3)

2.def func(**p):
     ----------
  func(a1,a2)   

EX:
num=3
num_2=9
num_3=7
def add(*a):
    print(a)
add(num,num_2,num_3)    

Ex:
def all(**Any):
    print(Any)
all(name="lav",age=12)    

Scope of Variable:
-------------------
1.Gobal Variable
----------------
-->This gobal variable can be used through out the program
Ex:
num=9
def func():
    print(num)
func()

2.Local Variable
----------------
-->This can be used only within in the fuction
-->It can't be access outside of the function
def func():
    num=9
    print(num)
func()
print(num)

Note
---
***If you want to change the global variable inside the function use keyword 'global'
-->It will change the variable value paramently inside and outside of the function
EX:
num=8
def func():
    global num
    num=89
    print(num)
func()
'''


    
















