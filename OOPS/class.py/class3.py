#Behaviour of methods
#there are 3 types
#1.Object methods
#2.Class methods
#3.Static methods
#1.Object methods :
''' These are used for defining,acessing and modifying the specific properties of an object '''
''' object methods are accessed only by using object reference only'''
'''self is the mandatory keyword '''
'''self is used for carrying the instance object address '''
class Bank:
    #generic properties
    bank_name='SBI'
    bank_ifsc=5145
    bank_roi=6
    bank_address='INDIA'
    #specific properties
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
    def customer_details(self):
        print(f'name of the customer is {self.name}')
        print(f'account of the customer {self.account}')
        print(f'balance of the customer {self.balance}')
        print(f'address of the customer{self.address}')
    def withdraw(self):
        amount=int(input('enter amount : '))
        if self.balance>=amount:
            self.balance-=amount
            print(f'withdraw amount {amount}')
            print(f'actual bank balance of the person is {self.balance}')
        else:
            print('insufficient balance')
            print(f'actual bank balance of the person is {self.balance}')
    def deposite(self):
        amount=int(input('enter amount : '))
        minimum_balance=500
        if amount>500:
            self.balance+=amount
            print(f'deposite is done {self.balance}')
        else:
            print('amount should be greater than 500 ')
vamsi=Bank('vamsikrishnaKayam',23651,75000,'banglore')
vamsi.customer_details()
vamsi.withdraw()
vamsi.deposite()
