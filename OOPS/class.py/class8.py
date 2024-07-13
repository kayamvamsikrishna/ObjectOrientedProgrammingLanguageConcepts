#method overloading
#It is a process of defining a method with a same name multiple times in a same class but with different arguments.
#In python method overloading is not possible
#But partially we can achieve it by providing default argument

#example
class Vamsi:
    def __init__(self):
        print('__init__ with no arguments')
    def __init__(self,a=10,b=20):
        self.a=a
        self.b=b
        print('__init__ with two arguments')
        #recently defined method will be concedered
vamsi=Vamsi(25,36)
krishna=Vamsi()