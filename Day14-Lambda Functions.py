
'''
Lambda Functions
----------------
-->this is also called as annonymous function
-->A lambda function can take n no.of arguments but having only one expression

Syntax:
lambda agruments : expersion

ex:
some=lambda an:an+5
print(some(100))

ex2:
some=lambda an,so,ok:an*so+ok
print(some(10,5,2))

filter()
--------
-->The filter function is built-in funtion used to filter elements from an itterables
such as list,tuple and set based on condition

Syntax:
filter(dunction,itterable)
-->This filter function returns filter object so we can convert that into other types
like list ,set and tuple

ex:
nums=[1,2,3,4,5]
rev=filter(lambda a:a%2==0,nums)
print(list(rev))

ex2:
nums=[1,2,3,4,5]
rev=filter(lambda a:a%2!=0,nums)
print(list(rev))




List Comprehension
--------------------
-->This offers shortest syntax when we want to create a new list from the old list

Syntax:
variable_name=[expreesion loop condition]
#codition is optional

ex1:
old_=[1,2,3,4,5,6,7]
new_=[j for j in old_ if j%2==0]
print(new_)

ex2:
old_=[1,2,3,4,5,6,7]
new_=[j for j in old_]
print(new_)




Dictionary Comprehension
------------------------
-->This offers shortest syntax when we want to create a new dict from the old dict

Syntax:
variable_name=[expreesion loop condition]
#codition is optional
ex1:
old_={1:2,3:4,5:11,7:8}
new_={i:j for (i,j) in old_.items() if j%2==0}
print(new_)

ex2:
old_={1:2,3:4,5:11,7:8}
new_={i:j for (i,j) in old_.items()
}
print(new_)

'''





















































































