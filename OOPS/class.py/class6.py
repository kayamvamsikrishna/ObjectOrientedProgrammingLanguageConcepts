#polymorphism
'''Polymorphism is the process of same method behaving in different ways '''
'''We can acheive polymorphism in two ways'''
#1.Method Overriding 
#2.Method Overloading
'''1.Method Overriding : 1.In case of inheritance,when we have to change the implementations/functionalities of parent class 
method in child class.
2.Redefine a method in child class with the same name as that of in parent class'''
#IMPORTANT PONTS:
'''1.If we use method overriding code then code reduntancy will be more'''
'''So we have to use chaining along with method overriding to reduce code redumdancy'''
#Chaining:
'''It is the process of calling the constructor or method of another class in current class'''
#We have two types of chaining:
'''1.Constructor Chaining '''
'''2.Method Chaining'''
#1.Constructor Chaining
'''It is the process of calling the constructor of another class constructor in current class'''
#We can perform in 2 ways 
#1.supermethod
#2.By class name
#1.supermethod :
'''super method is used only in case of inheritance'''
#Syntax:
''' super().constructor(argument)'''
#2.By class name
'''It is the process of calling the constructor by using class name and it can be done in case of inheritance and non inheritance'''
#syntax:
'''classname.constructor(argument)'''
#2.Method Chaining
'''it is the process of calling the another class method in the current class'''
#We can perform in 2 ways 
#1.supermethod
#2.By class name
#1.supermethod :
'''super method is used only in case of inheritance'''
#Syntax:
''' super().methodname(argument)'''
#2.By class name
'''It is the process of calling the constructor by using class name and it can be done in case of inheritance and non inheritance'''
#syntax:
'''classname.methodname(argument)'''
'''The FOLLOWING BEAUTIFUL EXAMPLE EXPLAINS THE ENTIRE METHOD OVERRIDING'''
#example by using super method of chaining
class Bank_V1:
    bank_name = 'SBI'
    bank_roi = 6
    bank_ifsc = 1245
    bank_address = 'India'

    def __init__(self, n, ac, b, ad):
        self.cname = n
        self.caccount = ac
        self.cbalance = b
        self.caddress = ad

    @classmethod
    def bank_details(cls):
        print(cls.bank_name)
        print(cls.bank_roi)
        print(cls.bank_ifsc)
        print(cls.bank_address)

    def customer_details(self):
        print(f'Name of the customer is {self.cname}')
        print(f'Account of customer is {self.caccount}')
        print(f'Address of customer is {self.caddress}')
        print(f'Balance of the customer is {self.cbalance}')

    @staticmethod
    def get_int_value():
        value = int(input('Enter int value: '))
        return value

    def withdraw(self):
        amount = self.get_int_value()
        if amount <= self.cbalance:
            self.cbalance -= amount
            print('Withdraw is successful')
        else:
            print('Insufficient balance')

    def deposit(self):
        amount = self.get_int_value()
        if amount > 0:
            self.cbalance += amount
            print('Deposit is successful')
        else:
            print('Amount should be more than one')


class Bank_V2(Bank_V1):
    bank_address = 'Bangalore'
    bank_mobile = 8074766625

    def __init__(self, n, ac, b, ad, pi):
        super().__init__(n, ac, b, ad)
        self.cpin = pi

    def customer_details(self):
        super().customer_details()
        print(f'Pin of customer is {self.cpin}')

    @classmethod
    def bank_details(cls):
        super().bank_details()
        print(f'Bank mobile is {cls.bank_mobile}')

    @classmethod
    def change_roi(cls):
        newroi = cls.get_int_value()
        cls.bank_roi = newroi
        print('ROI is changed')


# Creating an instance and testing the methods
vamsi = Bank_V2('vamsi', 45678, 1236555, 'nk', 4444)
vamsi.customer_details()
vamsi.bank_details()
