List DataType
-------------
-->List is collection of different datatypes that are enclosed in [] separatedv by ','
-->List is muttable

Ex:
all_type=[1,"python",[1,2]]
print(all_type)

List Methods
------------
1.append()
-->This is used to add a new item into the list but it will add in the last index  position
Syntax: variable_name.append(new item)
EX:
all_type=[1,"python",[1,2]]
print(all_type)
all_type.append(5)
print(all_type)
all_type.append("java")
print(all_type)

2.extend()
-->This is also add a item in the last index position it will give each value in the each index position
-->It will take only itterables
Syntax:variable_name.extend(new item)
Ex:all_type=[1,"python",[1,2]]
print(all_type)
all_type.extend([8,"language"])
print(all_type)
all_type.extend("language")
print(all_type)

3.pop()
-->This is used to delete the item from the list but it will delete based on index position
Syntax:variable_name.pop(index position)
EX:all_type=[1,2,"python","hello",7,8]
all_type.pop(3)
print(all_type)

4.remove()
-->this is used to delete the item  from the list but it will delete the direct item from list
Syntax:variable_name.remove(item value)
Ex:all_type=[1,2,"python","hello",7,8]
all_type.remove(8)
print(all_type)

5.insert()
-->this is used to add an item to the list at a particular position using indexing
syntax:variable_name.insert(new item )
ex:all_type=[1,2,"python","hello",7,8]
all_type.insert(2,5)
print(all_type)

6.sort()
-->this is used to sort the items paramently
Syntax:variable_name.sort
Ex:any_=[2,4,8,6,12]
any_.sort
print(any_)

7.sorted()
-->this is used to sort  the item  for that time only
Syntax:sorted(variable_name)
Ex:
any_=[2,4,8,6,12]
print(sorted(any_))
print(any_)

8.clear()
-->Removes all elements from the list.
Syntax:variable_name.clear()
Ex:any_=[2,4,8,6,12]
any_.clear()
print(any_)

9.index()
-->Returns the index of the first matching element.
Syntax:variable_name.index(item)
Ex:all_type=[1,2,"python","hello",7,8]
print(all_type.index(2))

10.count()
-->Returns the number of occurrences of a value.
Syntax:variable_name.count(item)
ex:all_type=[1,2,"python","hello",7,8,2,3,2,5]
print(all_type.count(2))

11.reverse()
-->Reverses the list
Syntax:variable_name.reverse()
Ex:any_=[2,4,8,6,12]
any_.reverse()
print(any_)

12.copy()
-->creates the copy of the list
Syntax:variable_name2=variable_name1.copy()
EX:any_=[2,4,8,6,12]
   many=any_.copy()
   print(many)


Indexing:
Ex:all_type=[1,"python",[1,2],[45,68,"java is a language",[1,23],90],"hello"]
print(all_type[3][2][10])
print(all_type[3][3][1])


**Muttable--->The dataType can be modified on that particular varaible
Ex:List
EX:all_type=[1,"python",[1,2]]
print(all_type)
all_type.append(5)
print(all_type)

**Immuttable--->the dataType can't be modified on that particular varaible
Ex:String
EX:so_="python is language
   print(so_.replace("python","java")
   print(so_)


Tuple DataType
-------------
-->Tuple is collection of different datatypes that are enclosed in () separatedv by ','
-->it is immuttable
Ex:many=(1,2,3,4,5,'python','java',[2,3],(8,7))
print(many)

In-Built Funtions:
1.len()
-->this is used to find the length of the tuple
syntax:len(variable_name)
Ex:many=(1,2,3,4,5,'python','java',[2,3],(8,7))
print(len(many))


2.count()
-->this is used to find how many time the item apperas in the tuple
syntax:variable_name.count(item)
Ex:many=(1,2,3,4,5,'python','java',[2,3],(8,7))
print(many.count(2))

3.index()
-->this is used to find the index value of particular item
Syntax:variable_name.index(item)
Ex:many=(1,2,3,4,5,'python','java',[2,3],(8,7))
print(many.index(5))

4.max()
-->Returns the largest element.
Syntax:max(variable_name)
Ex:num = (12, 45, 78, 23)
print(max(num))

4.min()
-->Returns the smallest element.
Syntax:min(variable_name)
Ex:num = (12, 45, 78, 23)
print(min(num))

5.sum()
-->Returns the sum of numeric elements
syntax:sum(Variable_name)
EX:num = (12, 45, 78, 23)
print(sum(num))

conversion tuple to list:
Ex:
many=(1,2,3,4,5,'python','java',[2,3],(8,7))
any=list(many)
print(any)











