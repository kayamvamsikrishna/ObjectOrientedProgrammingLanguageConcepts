#AGGREGRATION
'''It is the process of creating or using the object of one class in another class'''
'''In other words aggregation can be acheived by pointing to reference of object or
 creating the object of the class inside the other class'''
'''we can perform aggregation in two ways :
1) Creating an object in main space and using that in main class
2) Creating an object and using the object can be done in the main class'''
#case 1:
class Address:
    def __init__(self,l,h,t):
        self.city=l
        self.state=h
        self.country=t
    def display_address(self,):
        print(f'city name is {self.city}')
        print(f'state name is {self.state}')
        print(f'country name is {self.country}')
banglore=Address('banglore','karnataka','india')
class Student:
    def __init__(self,n,a,c,ad):
        self.sname=n
        self.sage=a
        self.sclass=c
        self.saddress=ad
    def student_details(self):
        print(f'name of the student is {self.sname}')
        print(f'age of the student is {self.sage}')
        print(f'class of the student is {self.sclass}')
        print(f'address of the student is {self.saddress}')
        print(f'address of the student is {self.saddress.display_address()}')
vamsikayam=Student('vamsikrishna',24,12,banglore)#here aggregation is done
vamsikayam.student_details()
bhanu=Student('bhanu',24,11,banglore)
#In the above case we are using the object in multiple times
#In the above case if we any developer are not use the object then it leads to memory wastage
#case 2:
class Address1:
    def __init__(self,l,h,t):
        self.city=l
        self.state=h
        self.country=t
    def display_address(self):
        print(f'city name is {self.city}')
        print(f'state name is {self.state}')
        print(f'country name is {self.country}')
class Student:
    def __init__(self,n,a,c):
        self.sname=n
        self.sage=a
        self.sclass=c
        a=input('enter city:')
        b=input('enter state:')
        d=input('enter country:')
        self.saddress=Address1(a,b,d)
    def student_details(self):
        print(f'name of the student is {self.sname}')
        print(f'age of the student is {self.sage}')
        print(f'class of the student is {self.sclass}')
        print(f'address of the student is {self.saddress}')
        print(f'address of the student is {self.saddress.display_address()}')
krishna=Student('krishna',16,10)
krishna.student_details()
#In the above case we can use the object at the point of time only due to this we can over come wastage of memory.