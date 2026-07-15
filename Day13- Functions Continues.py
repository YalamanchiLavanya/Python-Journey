'''
Passing by  value
-----------------
-->Passing by value means sending a value to a function. The function uses that value to perform its work.
Ex:
def some(a): 
    print(a)
some(8)    

Ex2:List
def some(a):
    for j in a:
        print(j)
some([1,2,3])

Ex3:tuple
def some(a):
    for j in a:
        print(j)
some((1,2,3))    

Ex4:
def some(a):
    print(a)
some("HELLO")

Passing by Reference:
--------------------
-->Passing by reference means sending a variable (reference) to a function instead of directly giving the value. The function can use that variable inside it.
Ex:
a=(1,2,3,4)
def some(a):
    for j in a:
        print(j)
some(a)

Return Keyword
--------------
-->In a function a return is executed then it will be exit from the function with certain returned values
-->It holds the value to thecalling function
-->WE can call it multiple times
-->The return keyword is used to send a result back from a function to the place where the function was called. It also stops the function.
ex:
def some(a):
    return 5+a
b=some(10)

Built-in function in python:
-----------------------------
-->Built-in functions are functions that are already available in Python. We can use them directly without creating our own functions.
import builtins
builtin_functions=[
    name for name in dir(builtins)
    if callable (getattr(builtins,name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}")

Recuersive  Function
---------------------
-->Recursive  function that call itself repeatedly until specified condition is met
-->A recursive function is a function that calls itself again and again until a stopping condition (base case) is reached.
Syntax:
def function_name(parameter):
    if condition:      #Base Case
           print/return statement
    else:
       print/return sattement
print(function_name(arguments))       

ex:
def func_name(num):
    if num==1:
        return 1
    else:
        return num*func_name(num-1)
num=8
print(func_name(num))

'''































