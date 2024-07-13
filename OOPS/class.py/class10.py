#Singleton class is a class which will have only one object in its life time
'''Singleton class properties can be acheived by only decorators'''
'''Beautiful Example'''
def plan(arg):
    d={}
    def inner():
        if arg not in d:
            d[arg]=arg()
        return d[arg]
    return inner
@plan
class Theator:
    def __init__(self):
        self.tickets=300
    def booking(self,n):
        if self.tickets>=n:
            self.tickets-=n
            print('Tickets are booked successfully')
            print(f'Available tickets are {self.tickets}')
        else:
            print('srry')
            print(f'Available tickets are {self.tickets}')
v=Theator()
v.booking(20)
k=Theator()
k.booking(30)