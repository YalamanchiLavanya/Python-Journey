'''
Student Marks Manager
'''
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




















