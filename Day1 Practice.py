
#Student Marks Manager

marks=[]
for mark in range(3):
    mark=int(input("enter the marks:"))
    marks.append(mark)
#print(marks)
#Insert 90 marks into the list    
marks.insert(0,90)

marks.extend([75,85])
#print(marks)

if 75 in marks:
    marks.remove(75)


marks.pop()

print(f'Final student marks{marks}')
print(f'count of the students marks{len(marks)}')


# Number List Analyser

numbers=[20,10,30,20,40,20]

#Sort the list in ascending order using sort()
numbers.sort()
print(numbers)

#Reverse the sorted list to produce descending order using reverse().
numbers.reverse()
print(numbers)

#Ask the user to enter a number to search for.
num=int(input("Enter a Number:"))

#Use a condition to check whether the number exists in the list
if num in numbers:
    #count(),index()
    print(numbers.count(num))
    print(numbers.index(num))
    
# Display the smallest value, largest value, and total using min(), max(), and sum(). 
print(min(numbers))
print(max(numbers))
print(sum(numbers))


#Even and Odd Number Separator 
numbers = [10, 15, 20, 25, 30, 35]

#Create two empty lists
even = []
odd = []

#Check every number using loop and %
for num in numbers:
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)

#Display even and odd lists
print("Even numbers:", even)
print("Odd numbers:", odd)

#Slicing
print("First three values:",numbers[:3])
print("Last three values:",numbers[-3:])

#Create backup using copy()
backup=numbers.copy()

#Clear original list
numbers.clear()

print("Original list:",numbers)
print("Backup list:",backup)


# Unique Name Manager

names = ["Asha", "Rahul", "Asha", "John", "Rahul"]

#Convert list into a set
names=set(names)

#Add Meera
names.add("Meera")

#Add Arun and Priya together
names.update(["Arun", "Priya"])

#Check if John exists and remove him
if "John" in names:
    names.remove("John")

#Try to remove David
names.discard("David")

#Display every unique name
print("Unique student names:")

for name in names:
    print(name)



#Course Student Comparison 

python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

#Students from both courses
both_courses = python_students.union(da_students)

#Students learning both courses
both = python_students.intersection(da_students)

#Students learning only Python
only_python = python_students.difference(da_students)

#Students learning only one course
only_one = python_students.symmetric_difference(da_students)

#Check if DA is a subset of Python
is_subset = da_students.issubset(python_students)

#Check if Python is a superset of DA
is_superset = python_students.issuperset(da_students)

#Check if sets are disjoint
is_disjoint = python_students.isdisjoint(da_students)

#Display results using loops
print("Students from both courses:")
for student in both_courses:
    print(student)

print("\nStudents learning both courses:")
for student in both:
    print(student)

print("\nStudents learning only Python:")
for student in only_python:
    print(student)

print("\nStudents learning only one course:")
for student in only_one:
    print(student)

print("\nRelationship Tests:")
print("DA is a subset of Python:", is_subset)
print("Python is a superset of DA:", is_superset)
print("Both sets are disjoint:", is_disjoint)







