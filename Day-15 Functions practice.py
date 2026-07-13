
#Remove dulipictaes from list
nums=[23,4,6,23,7,4]
empty_=[]
def removes_(nums,empty):
    for j in nums:
        if j not in empty_:
            empty_.append(j)
    print(empty_)
removes_(nums,empty_)

#Prime or not

num=7
count=0
def prime(num,count):
    for j in range(1,num+1):
        if num%j==0:
            count+=1
    if count==2:
        print("prime")
    else:
        ("Not Prime")    
prime(num,count)            

#count the number words in a string

some="Python is a programming language"
count=0
def count_(some,count):
    so=some.split(" ")
    for j in so:
        count+=1
    print(count)    
count_(some,count)    

#count capitals and small letters and spaces in the string

  some="Python Is a Programming Language"
cap_count=0
small_count=0
space_count=0
def cap_small(some,cap_count,small_count,space_count):
    for j in some:
        if j.isupper():
            cap_count+=1
        elif j.islower():
            small_count+=1
        else:
            space_count+=1
    print(cap_count)
    print(small_count)
    print(space_count)
cap_small(some,cap_count,small_count,space_count)    

#fibonacci series

num1=0
num2=1
limit=int(input("Enter your number:"))
def fibonacci(num1,num2,limit):
    print(num1,num2,end=" ")
    for i in range(1,limit+1):
        all = num1 + num2
        num1 = num2
        num2 = all
        print(all,end = " ")
fibonacci(num1,num2,limit)

#Palindrome or not

so=input("Enter you word:")
empty=""
def palindrome(so,empty):
    for j in so:
        empty=j+empty
    if empty == so:
        print(f"{so} is a palindrom")
    else:
        print(f"{so} is not a palindrom")
palindrome(so,empty)    

#Prefect number

  prefect_=int(input("Enter a Number:"))
all_sum=0
def prefect(prefect_,all_sum):
    for j in range(1,prefect_):
        if prefect_%j==0:
            all_sum+=j
    if all_sum==prefect_:
        print(f"{prefect_} is a prefect number")
    else:
        print(f"{prefect_} is a not prefect number")
prefect(prefect_,all_sum)

#Amrstrong or not

am_str=int(input("Enter a number:"))
length=len(str(am_str))
all_sum=0
def armstrong(am_str,length,all_sum):
    for j in str(am_str):
        all_sum+=int(j)**length
    if all_sum==am_str:
        print(f"{am_str} is a amstrong number")
    else:
        print(f"{am_str} is a amstrong number")
armstrong(am_str,length,all_sum)
'''

















