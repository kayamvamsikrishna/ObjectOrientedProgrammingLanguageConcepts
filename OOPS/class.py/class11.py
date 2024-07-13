#INHERITANCE
#IT IS THE PROCESS OF ACQUIRING THE PROPERTIES/FUNCTIONALITIES OF PARENT CLASS TO THE CHAILD CLASS
#SINGLE INHERITANCE
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks
#Multiple Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal:
    def walk(self):
        print("Mammal walks")

class Dog(Animal, Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.walk()   # Output: Mammal walks
dog.bark()   # Output: Dog barks
#Hierarchical Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks
cat.speak()  # Output: Animal speaks
cat.meow()   # Output: Cat meows
#Multi-level Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.walk()   # Output: Mammal walks
dog.bark()   # Output: Dog barks
#Hybrid Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Bird(Animal):
    def fly(self):
        print("Bird flies")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

class Bat(Mammal, Bird):
    def echo(self):
        print("Bat uses echo location")

dog = Dog()
bat = Bat()
dog.speak()  # Output: Animal speaks
dog.walk()   # Output: Mammal walks
dog.bark()   # Output: Dog barks
bat.speak()  # Output: Animal speaks
bat.walk()   # Output: Mammal walks
bat.fly()    # Output: Bird flies
bat.echo()   # Output: Bat uses echo location
