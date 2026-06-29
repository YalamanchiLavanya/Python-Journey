
Type Conversion
----------------
-->This is process of converting one data type to another data type
1.Int-->String,Float
-->It can be convert into by using built-in functions like
*str()
*float()
Ex:
num=89
print(type(num))

so=str(num)
print(type(so))

num_2=float(num)
print(type(num_2))

2.Float-->String,Int
-->It can be convert into by using built-in functions like
*str()
*int()
EX:
num=89.56
print(type(num))

so=str(num)
print(type(so))

num_2=int(num)
print(type(num_2))

3.String-->Int,Float,List,Tuple
-->It can be convert into by using built-in functions like
*float()
*int()
*list()
*tuple()
EX:
str="23456"
print(type(str))

num=int(str)
print(type(num))

num_1="90.87"
num_2=float(num-1)
print(type(num_2))

list_=list(str)
print(type(list_))

so=tuple(str)
print(type(so))

4.List-->String,Tuple,Dictionary
-->It can be convert into by using built-in functions like
*str()
*tuple()
*
Ex:
so=["l","a","v",a","n","y","a"]
print(type(so))

go=str(so)
print(type(go))

so=['l','a','v','a','n','y','a']
text_="".join(so)
print(text_)

come=tuple(so)
print(type(come))

pyth_=[('a',1),('b',2)]
conv_=dict(pyth_)
print(conv_)
print(type(conv_))


5.Tuple-->String,List
-->It can be convert into by using built-in functions like
*str()
*list()
Ex:
so=(1,2,3,4,5)
print(type(so))

go=str(so)
print(type(go))

so=('l','a','v','a','n','y','a')
text_="".join(so)
print(text_)

come=list5(so)
print(type(come))

Built-in Functions
---------------------
1.int()
2.float()
3.str()
4.list()
5.tuple()
6.dict()

6.Dictionary --> List,Tuple,String
-->It can be convert into by using built-in functions like
*list()
*tuple()
*str()
Ex:
student = {"name": "Lavanya", "age": 21}
go= list(student)
print(lst)

tup = tuple(student)
print(tup)

text = str(student)
print(text)

7.set-->List,Tuple,String
-->It can be convert into by using built-in functions like
*list()
*tuple()
*str()
ex:
s = {10, 20, 30}
print(list(s))
print(tuple(s))
print(str(s))

8.Integer-->Boolean
print(bool(10))
print(bool(0))

9.Float → Boolean
print(bool(5.5))
print(bool(0.0))

10.String → Boolean
print(bool("Python"))
print(bool(""))

11.List → Boolean
print(bool([1,2,3]))
print(bool([]))

12.Tuple → Boolean
print(bool((1,2)))
print(bool(()))

13.Dictionary → Boolean
print(bool({"a":1}))
print(bool({}))

14.Set → Boolean
print(bool({1,2}))
print(bool(set()))

15.Boolean → Integer
print(int(True))
print(int(False))





