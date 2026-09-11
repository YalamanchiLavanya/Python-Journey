'''
Scenario to understand (*args and **kwargs)

Modules -->some intresting cases -->Projects(Virtual Assistant,Email Automation
OOP-->Github(branch)


#Employee Details

def employees(*names,**settings):
    """Employee Details Along with their Settings"""
    print("Employee Names")
    for employee in names:
        print('----------')
        print('-',employee)


    for key,value in settings.items():
        print(names,'-',key,":",value)
names=input("Names :")
settings=input("setting:")
employees(names,
          department=["operations","HR","Finacial"],
          experince_letters=True,
          salary=True)
projects

Module

OOP

Organization --->class

Encapusulation,Inheritance,polymorphism

Employees --->Functions  (Methods)
Performance metrics --->Function
Increment--->Function

emp1,emp2,emp3------->objects

Module
=======
-->A Module is siimple python file(reusable,orgainsed code)

import --keyword

Employee Details/Performance (employee.py)
    -->employee function
    -->performnace function
    -->Increment/Leadership/Learning function
'''

#Employee Details

def employees(*names,**settings):
    """Employee Details Along with their Settings"""
    print("Employee Names")
    for employee in names:
        print('----------')
        print('-',employee)

    for key,value in settings.items():
        print(names,'-',key,":",value)
        

#if __name__="__main__":
details={"Organization":"Codegnan",
         'year':2018,
         'branches':['Vijayawada','Hyderabad','Vizag']}
print(__name__)      #Dunder methods --magic Methods 






























