#Every python filr is a --> module -->Import Keyword --> __name__
'''
import Day4
print(dir(Day4))    #dir --->directory will return all avaiable methods,attributes4

print(type(Day4.employees))
print(type(Day4.details))


Day4.employees("lavanya","likhith","Likku",
          department=["operations","HR","Finacial"],
          experince_letters=True,
          salary=True)

Day4.employees("Lavnaya",destination="Student",Location="Vizag")
print(Day4.details)
print(Day4.details.keys())
print(Day4.details['Organization'])

#Update
Day4.details.update({'batches':['pfs','jfs','da'],'employess':200})
print(Day4.details)


#from Keyword

from Day4 import employees,details

details.update({'batches':['pfs','jfs','da'],'employess':200})
#print(details)

print(Day4.__doc__)   #It return Docstring from the given module
'''

#Built_in Modules -->Math,random,os,time,datetime

#we download modules from -->pypi (Python Package Index)

#Build a QR Code Scanner using Python -->LinkedIn URL

#pyqrcode,png

#pip install pyqrcode
#pip install pypng

import pyqrcode
import png

#Create a QRcode by giving a link
link="https://www.linkedin.com/in/lavanya-yalamanchi/"
qr=pyqrcode.create(link)
#print(qr)
qr.png("myqr.png",scale=10)s


#Personal Business card -->name,phone,





























































