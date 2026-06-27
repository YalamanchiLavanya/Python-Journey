Dictionary
-----------
-->Dictionary is a key:value pair seperated by ':'
-->key are to be unique
-->duplicate keys not allowed
-->in the place of keys we to use immuttable data type
-->Dictionary is the muttable
-->it represented using {}

Syntax:variable_name={key:value}
Ex:details_={"name":"lavanya",
             1:"number",
             (12.23):[1,2]}

Ex:
details_={"name":"lavanya",
             1:"number",
             (12.23):[1,2]}
print(details_)

Ex2:
icic_details_={"name":"lavanya","number":2345678889,"Adhar":456789123678,
               "Acc no":56789012345,
               "ATM PIN":4567}
print("Welcome to ATM")
user_pin=input("Enter you 4 digit pin:")
if user_pin in icic_details_["ATM PIN"]:
    print("\n1.deposite \n2.withdraw")
else:
    print("Invalid pin")


Methods of Dictionary:
----------------------
1.keys()
-->This used to get all the keys from the dictionary
Syntax:variable_name.keys()
Ex:
details_={"name":"lavanya",
             1:"number",
             (12.23):[1,2]}
print(details_.keys())

2.values()
-->This is used to get all the values the dictionary
Syntax:variable_name.values()
Ex:
details_={"name":"lavanya",
             1:"number",
             (12.23):[1,2]}
print(details_.values())

3.itemes()
-->This is used to get all the key and value pairs from the dictionary
Syntax:variable_name.items()
Ex:
details_={"name":"lavanya",
             1:"number",
             (12.23):[1,2]}
print(details_.items())

4.clear()
-->This is used to clear the all the pairs in the dictionary
Syntax:Variable_name.clear()
Ex:
details_={"name":"lavanya",
          1:"number",
          (12.23):[1,2],
          "Age":22,
          "Area":"srikakulam"}
print(details_.clear())

5.update()
-->This is used the new values to the same key
Syntax:variable_name.update({old key : new values})
Ex:
details_={"name":"lavanya",
          1:"number",
          (12.23):[1,2],
          "Age":22,
          "Area":"srikakulam"}
details_.update({'name':'likhitha'})
print(details_)

EX:
details_={"name":"lavanya",
          1:"number",
          (12.23):[1,2],
          "Age":22,
          "Area":"srikakulam"}
details_.update({'Mob NO':1234567890})
print(details_)

6.get()
-->Returns the value of the specified key.
Syntax:get(Variable_name)
EX:
details_={"name":"lavanya",
          1:"number",
          (12.23):[1,2],
          "Age":22,
          "Area":"srikakulam"}
print(details_.get('name'))

7.pop()
-->Removes the specified key and returns its value
Syntax:variable_name.pop(key)
ex:
details_={"name":"lavanya",
          1:"number",
          (12.23):[1,2],
          "Age":22,
          "Area":"srikakulam"}
age = details_.pop("age")
print(age)
print(details_)

8.popitem()
-->Removes and returns the last inserted key-value pair.
Syntax:variable_name.popitem()
ex:
details_={"name":"lavanya",
          1:"number",
          (12.23):[1,2],
          "Age":22,
          "Area":"srikakulam"}

print(details_.popitem())
print(details_)

##How to access the values in the dictionary
EX:
details_={"name":"lavanya",
          1:"number",
          (12.23):[1,2],
          "Age":22,
          "Area":"srikakulam"}
print(details_['Area'])



SET DataType
-------------
-->Set is a collection of un-ordered Elements that are seperated by ,
-->set is muttable
--> it can remove duplicate value by itself
-->it was represented in { }
EX:
go={1,2,3,4,2,1,3}
print(go)

Set methods
-----------
1.union() or (|)
-->This is used to combine the elements from both sets
Syntax:
*variable1.union(variable2)
*variable1 | variable2
EX:
go={1,2,3,4,2,1,3}
come={2,3,4,5,6,8}
print(go | come)
print(go.union(come))

2.intersection() or (&)
--> This is used to find the common elements from both sets
Syntax:
*variable1.intersection(variable2)
*variable1 & variable2
Ex:
go={1,2,3,4,2,1,3}
come={2,3,4,5,6,8}
print(go & come)
print(go.intersection(come))

3.symmetric Difference  or (^)
-->This is used to find diffrent elements from both sets
Syntax:
*variable1.symmetric_difference(variable2)
*variable1 ^ variable2
Ex:
go={1,2,3,4,2,1,3}
come={2,3,4,5,6,8}
print(go ^ come)
print(go.symmetric_difference(come))

4.diifference()
-->Returns elements that are in the first set but not in the second
Syntax:Variable1.difference(variable2)
EX:
go = {1,2,3,4,2,1,3}
come = {2,3,5,6}
print(go.difference(come))
Built-in Functions
---------------------
1.add()
--> This is used to add new elements to the set
Syntax:Variable_name.add(element)
Ex:
go={1,2,3,4,2,1,3}
go.add(9)
print(go)

2.max()
-->This is used to find the max element in the set
Syntax:max(variable_name)
Ex:
go={1,2,3,4}
print(max(go))

3.min()
-->This is used to find the min element in the set
Syntax:min(variable_name)
Ex:
go={1,2,3,4}
print(min(go)

4.remove()
-->This is used to delete
an element from the set
--->if the element is not there in the set it throws an error
Synatx:variable_name.remove(element)
EX:
go={1,2,3,4,2,1,3}
go.remove(1)
print(go)

5.pop()
-->it delete the first Index value
Syntax:
variable_name.pop()
Ex:
go={5,1,2,3,4}
go.pop()
print(go)

6.discard()
-->This is used to delete an element from the set
--->if the element is not there in the set it  not throws an error
Syntax:
varaible_name.discard(element)
EX:
go={1,2,3,4,2,1,3}
go.discard(5)
print(go)

7.update()
-->Adds multiple elements to the set
Syntax:variable_name.update()
Ex:
go = {1,2,3,4,2,1,3}
go.update({5,6,7})
print(go)

8.clear()
-->Removes all elements.
Syntax:variable_name.clear()
EX:
go = {1,2,3,4,2,1,3}
go.clear()
print(go)

9.copy()
-->Creates a copy of the set.
Syntax:new_variable=old_variable.copy()
EX:
go = {1,2,3,4,2,1,3}
new_go = go.copy()
print(new_go)















