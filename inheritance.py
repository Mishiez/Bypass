#Parent class
class Animal:
    def speak(self):
        print("Animal is speaking")

#Child Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

a = Animal()


d = Dog()
d.speak()