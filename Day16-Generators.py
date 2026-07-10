'''
Generators
----------
-->This generator is a special function that returns the itertor.
Instead of returning all the values at once
-->Here we are going to use yeild keyword
-->This process is know as lazy evolution

Ex:
def some():
    yield 1
    yield 2
    yield 3
so=some()
print(next(so))
print(next(so))
print(next(so))

Working of Generators:
----------------------
-->When a function is called
-->It does not execute the function immediately....
-->It will genertae the object
-->Then the function will pauses at each yield....
-->When the next() is called again,execution resumes from where it stopped

EX:

def demo():
    print("start")
    yield 1
    print("Middle")
    yield 2
    print("End")
    yield 3
how=demo()
print(next(how))
print(next(how))
print(next(how))

Ex2:With Generator

def demo(so):
    for i in range(so):
        yield i*i
how=demo(5)
print(next(how))
print(next(how))
print(next(how))
print(next(how))
print(next(how))

Ex3:without generator

def demo(so):
    for i in range(so):
        print(i*i)
demo(5)


Difference b/w function and Generator

Function
----------
-->return
-->return complete result
-->function will end after the return the values
-->more memory usage
-->This function never resume 
Generator
----------
-->yield
-->return one value at once
-->pauses after every yield
-->less memory usage
-->Resume after next()

Yield keyword:
--------------
-->It will produce the values
-->but the yeild pauses the function
-->the yield will save the functions current state
-->yeild wii continues execution  where it stoped.....

next() function
---------------
-->The next() function is used to retrieve the next value from a generator

Ex:

def demo(so):
    for i in range(so):
        yield i*i
how=demo(5)
print(next(how))
print(next(how))

Stop Iteration:
---------------
-->Calling next() function after all values retrieve
then it will rise 'StopIterarion'Exception

ex:
def demo(so):
    for i in range(so):
        yield i*i
how=demo(5)
print(next(how))
print(next(how))
print(next(how))
print(next(how))
print(next(how))
print(next(how))


Generator Expression
--------------------
-->The generator expression is simliar to a list comprehension
but uses parenthesis() instead of []

Ex:
gen=(x*x for x in range (5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

'''





























    
   
