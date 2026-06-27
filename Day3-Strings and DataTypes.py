
Data Types
----------
--->Int
Ex:num=7

--->Float
Ex:num_2=6.44

STRINGS
-------
-->String is a sequence of character that are enclosed in ''," ",''' '''.
-->String is immutable
Ex:so='apple'
Ex:any_="@, . 3"

Concatination
-------------
-->Here the  + (addition operator) act as to concatinate more than 2 strings
Ex:
so="python"
any_="is a language"
print(so+any_)

Indexing
--------
-->This is used to access the particular character in the string by passin index position value
--> Index starts from 0 ....
--> we have negative Indexing to count the positions from the last to first
Ex:
so="python is a language"
print(so[12])
print(so[-2])


Methods of strings
------------------
1.replace()
-->This method is used to replace or change any sub string  in that particular string in only runtime
Syntax:  variable_name.replace("old string","new string",count)

Ex1:
so="python is a language"
print(so.replace("python","java"))
print(so)

Ex2:
so="python is a language"
print(so.replace("a","A",2))
print(so)

2.join()
-->This method used to add a new substring after each character in string
Syntax: "new string".join(variable_name)

Ex1:so="python is a language"
print("-".join(so))
print(so)

Ex2:
so="python is a language"
print("*".join(so))
print(so)

3.split()
-->This method can divide the string into different index int list, based on the string pass by us
Syntax: variable_name.split("substring")

Ex1:
so="python is a language"
print(so.split(" "))
print(so)

Ex2:
so="python is a language"
print(so.split("is"))
print(so)

4.count()
-->This method used to count the substring or particular string and also specify the index position
syntax:variable_name.count("sub string",starting index,ending index)
Ex1:
so="python is a language"
print(so.count("a"))

Ex2:
so="python is a language"
print(so.count('a',0,12))


String Built-in  Functions
--------------------------
1.len()
-->This will find Length of the string,which is number of character present in the string
Syntax: len(variable_name)

Ex:
so="python is a language"
print(len(so))

2.max()
-->we will get the max character in the string
Syntax:max(variable_name)

Ex:so="python is a language"
print(max(so))

3.min()
-->we will get min character in the string
Syntax: min(variable_name)
Ex:
so="python is a language"
print(min(so))



#Convert 24hours time into normal time

time_="16:56"
parts_=time_.split(":")
print("this time",time_,"is convert into this",int(parts_[0])-12,":",parts_[1],"pm")

