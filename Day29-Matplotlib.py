''' 
Matplotlib
----------
-->Matplotlib libary is a python libary that provides
functionality to create charts,bars,pie charts and data visulization

Line Plot
----------
Ex1:
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,15,30,5]

plt.plot(x,y)
plt.show()

Ex2:
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,15,30,5]

plt.plot(x,y)
plt.title('Sample Table')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

Ex3:
import matplotlib.pyplot as plt

x=[2026,2025,2024,2023,2022]
y=[120,150,135,30,90]

plt.plot(x,y)
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of Cars')
plt.show()

Bar plot
--------
Ex1:

import matplotlib.pyplot as plt

x=[2026,2025,2024,2023,2022]
y=[120,150,135,30,90]

plt.bar(x,y)
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of Cars')
plt.show()

Ex2:

import matplotlib.pyplot as plt

x=[2026,2025,2024,2023,2022]
y=[120,150,135,30,90]

plt.bar(x,y,color='yellow',edgecolor='black')
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of Cars')
plt.show()

Ex4:
import matplotlib.pyplot as plt

x=[2026,2025,2024,2023,2022]
y=[120,150,135,30,90]

plt.bar(x,y,color='yellow',edgecolor='black')
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of Cars')
plt.show()


pie plot
--------
Ex1:
import matplotlib.pyplot as plt
subjects_ = ['python','java','c']
stu_ = [69,79,50]

plt.pie(stu_,labels=subjects_,autopct='1%.1f%%')
plt.legend(subjects_)
plt.title('courses')
plt.show()


Ex2:
import matplotlib.pyplot as plt
subjects_ = ['python','java','c']
stu_ = [69,79,50]

plt.pie(stu_,labels=subjects_,colors=['red','yellow','purple'],autopct='1%.1f%%')
plt.legend(subjects_)
plt.title('courses')
plt.show()

Scatter plot
------------
import matplotlib.pyplot as plt
x=['BMW','SWIFT','TOYOTO']
y=[120,150,135]

plt.scatter(x,y,color='pink')
plt.title('Car Sales')
plt.xlabel(' Years')
plt.ylabel('Number of Cars')
plt.show()


All Plots
---------

import matplotlib.pyplot as plt
x=['BMW','SWIFT','TOYOTO','AUDI']
y=[120,150,135,200]

plt.scatter(x,y,color='black')
plt.title('Car Sales')
plt.xlabel(' Years')
plt.ylabel('Number of Cars')
plt.show()


plt.plot(x,y)
plt.title('Car Sales')
plt.xlabel(' Years')
plt.ylabel('Number of Cars')
plt.show()


plt.bar(x,y,color='red',edgecolor='black')
plt.title('Car Sales')
plt.xlabel(' Years')
plt.ylabel('Number of Cars')
plt.show()


plt.pie(y,labels=x,autopct='1%.1f%%')
plt.legend(x)
plt.title('Car Sales')
plt.show()

Histogram
----------
Ex1:

import matplotlib.pyplot as plt

y=[10,40,20,50]

plt.hist(y,bins=20)
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of cars")
plt.show()

Ex2:

import matplotlib.pyplot as plt

y=[10,40,20,50]

plt.hist(y,bins=10)
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of cars")
plt.show()


'''











