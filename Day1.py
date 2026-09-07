
Triple Quotes-->Multi line cooments-->Doc string

variables --> operators --> Datatypes(Numeric,Collections(str,list,Tuples,Dictionary)
--> Control Block(logic) (if,elif,else,for,while,break,continue,pass)--> procedure Oriented Programming
(Functions)--> OOP(Class,Objects)

Slicing:[start,end]


name="codegnan"
batch=23
email_id="saketh@codegnan.com"
print(len(email_id))

#slicing
print(email_id[7:15])

email_ids=['saketh@codegnan','lavanya@codegnan','lohitha@codegnan','likki@codegnan']
print(len(email_ids))
print(email_ids[1])
# last two email ids
print(email_ids[-2:])
print(type(email_ids[-2:]))

print(email_ids[-2])
print(type(email_ids[-2]))

#let store 3 more mail ids into above at a time
email_ids.extend(['pallavi@codegnan','sony@codegnan','varsha@codegnan'])
print(email_ids)


#Access each mail_id one by one -->loop
for mail in email_ids:
    #print(mail)
    print(f'email_id of person is {mail}')


#Store the email_id with revalant  user_names

users={}
print(type(users))

#get the above user id into empty dictionary
users=dict.fromkeys(email_ids)
print(users)

#All python builtin datatypes are Built_in Functions
#(int,float,str,list,tuple,dict,set,bool)


print(users)
for i in range(len(email_ids)):
               #print(i,email_ids[i])
               users[i+1]=email_ids[i]
print(users)
               

#enumerate--It provides by default a counter object
#(you can store in desired collection)
#In python everything is a object
#Functions-->first class Objects
# a function can pass  another function as an argument and input  and a function can return an another function
# A set  an Unordered Collection as no indexing
data=dict(enumerate(email_ids,1))
print(data)    
 


















