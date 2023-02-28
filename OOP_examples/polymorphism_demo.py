"""
Polymorphism is the ability of an object to be processed differently based upon its type.

It can be achieved through inheritance where each child class has methods with the same identifier as their parent but with a different implementation, though a technique known as overriding. 

It can also be achieved though interfaces, whereby two classes are said to implement a particular interface, meaning that you can rely upon it having a certain method (or set of methods) allowing you to treat those objects as if they were the same type, for the purpose of utilising that method.

In the example below a list is created whose members are objects of different types: Animals, Cats and Dogs. All have a speak() method and when each has its speak() method invoked they will be processed differently depending upon the type of object that they actually are.
"""

class Animal:
  
  def speak(self):
    print("Hello")

class Dog(Animal):

  def speak(self):
    print("Woof!")

class Cat(Animal):

  def speak(self):
    print("Meow!")


list_of_animals = [Dog(), Dog(), Cat(), Cat(), Animal()]

for a in list_of_animals:
  a.speak()

