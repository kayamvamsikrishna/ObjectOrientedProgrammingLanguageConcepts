#example by using class name of chaining
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

    def bank_details(self):
        print(self.bank_name)
        print(self.bank_roi)
        print(self.bank_ifsc)
        print(self.bank_address)

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
        Bank_V1.__init__(self,n, ac, b, ad)
        self.cpin = pi

    def customer_details(self):
        Bank_V1.customer_details(self)
        print(f'Pin of customer is {self.cpin}')

    @classmethod
    def bank_details(cls):
        Bank_V1.bank_details(cls)
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
