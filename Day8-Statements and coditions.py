
Statements
------------
-->Statements are instructions written in a program that tell Python what action to perform. Every line of executable code in Python is called a statement.
-->Statements are three types
1.Conditions
2.Controls
3.Loops

**Conditions
------------
-->Conditional statements are used to make decisions in a program. They execute different blocks of code depending on whether a condition is True or False.
1.if
----
-->This is used to check the condition is true or not
Syntax:if(condition):
          statement
Ex:
num=10
if(num%2==0):
    print(f"{num} is a even number")

2.if else
---------
-->Else is the fall-back statement in case the if condition is false ,then this else will be executed
Syntax:if(condition):
         statement
       else:
         statement
EX:
num=39
if(num%2==0):
    print(f"{num} is a even number")
else:
    print(f"{num} is odd number")

Ex2:
likki_ICIC_details={"ATM PIN":'0987'}
pin_=input("Enter your digit atm pin")
if pin_ in likki_ICIC_details['ATM PIN']:
    print("welcome to ICIC Atm")
else:
    print("You Entered Incorrect Pin")

3.nested if
-------------
-->if inside the another if is called nested if
Syntax:if(condition): 
        if(condition):
         statement
        else:
         statement
Ex:
likki_ICIC_details={"ATM PIN":'0987'}
pin_=input("Enter your digit atm pin:")
if len(pin_)==4:
    if pin_ in likki_ICIC_details['ATM PIN']:
        print("welcome to ICIC Atm")
    else:
        print("You Entered Incorrect Pin")
else:
    print("Pls Enter 4 digit pin")

4.elif
-->
Syntax:if(condition):
         statement
       elif(condition):
         statement
       else:
         statement
Ex:
marks_=int(input("Enter your Marks:"))
if marks_ >=90:
    print("A+")
elif marks_>=80:
    print("A")
elif marks_>=70:
    print("B+")
elif marks_>=60:
    print("B")
elif marks_>=40:
    print("c")
else:
    print("You are Fail")
    
Examples:

#vowel or not
char_=input("Enter Char:")
vowel_=['a','e','i','o','u','A','E','I','O','U']
if char_ in vowel_:
    print("Vowel")
else:
    print("Not a Vowel")

#max of 3 numbers
num_1=int(input("Enter interger:"))
num_2=int(input("Enter interger:"))
num_3=int(input("Enter interger:"))
if num_1>num_2 and num_1>num_3:
    print(f"{num_1} is max")
elif num_2>num_1 and num_2>num_3:
    print(f"{num_2} is max")
else:
    print(f"{num_3} is max")



