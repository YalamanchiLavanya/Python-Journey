'''
Loop Statements
---------------
-->Loops are two types
1.For Loop
-----------
-->For Loop is used to itterate over a sequence ,list,tuple
-->Why the variable is not defined in anywhere and not an error
**Because it is instance variable
Syntax:
Examples:
---------
**String
---------
EX:any_="python is language"
for j in any_:
    print(j)
    
**List:
-------
any_=[1,2,3,4,5,6]
for j in any_:
    if j%2==0:
        print("even")
    else:
        print("odd")
        
**Tuple
--------
any_=(1,2,3,4,5,6,'a','b')
for j in any_:
   print(j)

**Dictionary
-------------
any_={"Name":"likki","age":"34"}
for j in any_.items():
   print(j)

any_={"Name":"likki","age":"34"}
for j in any_.keys():
   print(j)

any_={"Name":"likki","age":"34"}
for j in any_.values():
   print(j)

else in for loop:
-----------------
-->The else block will be executed after the for loop, but incase the loop is breaked then it will never entered into the else block
EX1:
any_=[1,2,3,4,5,6]
for j in any_:
    print(j)
else:
    print("Program ended")
    
EX2:
any_=[1,2,3,4,5,6]
for j in any_:
    print(j)
    if j==3:
        break
else:
    print("Program ended

Range
------
-->Range is a in-built function that is used to generate a squence upto a liit
Syntax--->range(start,end,step)
Ex1:
for j in range(1,51):
    if j%2==0:
        print(j)
Ex2:
for j in range(1,51,2):
        print(j)

        
2.While Loop
-------------
-->The will loop will execute until the condition became true
-->It is a combination if and for
Ex1:
i=1
while i<5:
    print(i)
    i+=1
Ex2:
i=1
while i<5:
    print(i)



Control Statements
------------------
1.break
---------
-->The break statement iis used to exit from the loop
Ex:
any_=[1,2,3,4,5,6]
for j in any_:
    print(j)
    if j==3:
        break
else:
    print("Program ended")

2.continue
----------
-->The continue will skip the current iteratiom of condition is match
Ex:
any_=[1,2,3,4,5,6]
for j in any_:
    if j==3:
        continue
    print(j)
else:
    print("Program ended")

3.pass
-->Pass is nothing but Space holder
-->It places an error when no statement in the loops or if conditions
EX:
any_=[1,2,3,4,5,6]
for j in any_:
    if j==3:
        pass

Assert Keyword
---------------
-->It will used to check the condition ,but it will raise an error incase it is flase....
Ex1:num=10
assert num>0
print(f"{num} is positive  number")

Ex2:
num=10
assert num<0,'has to be zero'

Ex3:
age=int(input("Enter your age:"))
assert age>=18,'you must have 18 years'

'''





















