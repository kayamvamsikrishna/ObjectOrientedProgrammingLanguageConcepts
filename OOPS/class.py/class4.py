#2.Class methods
''' Class methods are used for accessing and modifying the class members '''
''' It takes a mandatory argument which is nothing but cls '''
'''cls is used for accessing and modifying the class '''
''' By using this class method we can access and modify the class members directly by using class reference and object reference'''
'''class methods are decorated by using the class method decorator'''
#3.StaticMethods
''' Static methods are neither belongs to class nor belongs to objecta '''
'''no need of pasing any argument like self and cls'''
'''By using static method we cannot access or modify the class state or object state'''
'''these methods are defined just to get some data while execution of object method or class method '''
'''Static methods are decorated by using the static method decorator'''
class Bank:
    #class properties
    bank_name='SBI'
    bank_ifsc=1245
    bank_roi=6
    bank_address='Hydrabad'
    #specific properties
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
    @classmethod
    def bank_details(cls):
        print(cls.bank_name)
        print(cls.bank_ifsc)
        print(cls.bank_roi)
        print(cls.bank_address)
    @staticmethod
    def get_int_value():
        intvalue=int(input('Enter int value:'))
        return intvalue
    @classmethod
    def modify_roi(cls):
        print(cls)
        new_roi=cls.get_int_value()
        cls.bank_roi=new_roi
        print('roi is modified')
    def withdraw(self):
        amount=self.get_int_value()
        if self.balance>=amount:
            self.balance-=amount
            print('withdraw is successfull')
        else:
            print('in sufficient balance')
            print(f'balance is {self.balance}')
    #object method
    def customer_details(self):
        print(f'name of the customer is {self.name}')
        print(f'account of the customer is {self.account}')
        print(f'balance of the customer is {self.balance}')
        print(f'address of the customer is {self.address}')
janu=Bank('janu',8954,10000,'delhi')
anu=Bank('anu',6642,20000,'chennai')
Bank.bank_details()
Bank.modify_roi()
print(janu.bank_roi)
print(anu.bank_roi)
print(Bank.bank_roi)
janu.withdraw()