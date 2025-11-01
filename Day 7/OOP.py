# # ========================================
# # 🧠 Object-Oriented Programming in Python
# # ========================================

# # ----------------------------------------
# # 1️⃣ CLASS AND OBJECT
# # ----------------------------------------
# print("=== CLASS AND OBJECT ===")

# class Student:
#     # Class attribute
#     college = "ABC Institute"

#     # Constructor
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

#     # Instance method
#     def display(self):
#         print(f"Name: {self.name}, Roll: {self.roll}, College: {Student.college}")

# # Creating objects
# s1 = Student("Tushar", 101)
# s2 = Student("Aarav", 102)

# s1.display()
# s2.display()

# print()  # ----------------------------------------

# # ----------------------------------------
# # 2️⃣ CONSTRUCTORS (TYPES)
# # ----------------------------------------

# print("=== CONSTRUCTORS (TYPES) ===")

# # (a) Default Constructor – No arguments
# class DefaultDemo:
#     def __init__(self):
#         print("This is a Default Constructor")

# obj1 = DefaultDemo()

# # (b) Parameterized Constructor – Takes arguments
# class ParameterizedDemo:
    
#     def __init__(self,name, age):
#         print("This is a Parameterized Constructor")
#         self.name = name
#         self.age = age
#     def __init__(self, name, age=20):
#         print("This is a Parameterized1 Constructor")
#         self.name = name
#         self.age = age
#     def __init__(self):
#         print("This is a Default Constructor")
#         self.name = ""
#         self.age = 0

#     def show(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# obj2 = ParameterizedDemo("Tushar")
# obj2.show()

# # (c) Constructor Overloading Simulation (using default args)
# class OverloadDemo:
#     def __init__(self, a=None, b=None):
#         if a is not None and b is not None:
#             print("Sum:", a + b)
#         elif a is not None:
#             print("Single value:", a)
#         else:
#             print("No values passed")

# obj3 = OverloadDemo()
# obj4 = OverloadDemo(5)
# obj5 = OverloadDemo(5, 10)

# print()  # ----------------------------------------

# ----------------------------------------
# 3️⃣ INHERITANCE (TYPES)
# ----------------------------------------

# print("=== INHERITANCE (TYPES) ===")

# # (a) Single Inheritance
# class Parent:
#     n=20
#     def func1(self):
#         print("This is Parent class")

# class Child(Parent):
#     def func2(self):
#         print("This is Child class")
#     def printN(self):
#         print(self.n)

# obj = Child()
# obj.func1()
# obj.func2()
# obj.printN()

# print()  # ----------------------------------------

# class Vehicle:
#     speed=0
#     average=0
#     name=""
#     def printInfo(self):
#         print(self.name," ",self.speed," ",self.average)

# class Car(Vehicle):
#     def __init__(self,name,speed,avg):
#         self.speed=speed
#         self.average=avg
#         self.name=name

# class Bike(Vehicle):
#     def __init__(self,name,speed,avg):
#         self.speed=speed
#         self.average=avg
#         self.name=name

# b=Bike("ABC",20,50)
# c=Car("XYZ",90,50)

# b.printInfo()
# c.printInfo()

# # A ->  B ->  C

# # (b) Multilevel Inheritance
# class Grandparent:
#     def grand(self):
#         print("This is Grandparent class")

# class Parent(Grandparent):
#     def parent(self):
#         print("This is Parent class")

# class Child(Parent):
#     def child(self):
#         print("This is Child class")

# # class ABC(Child):


# obj = Child()
# obj.grand()
# obj.parent()
# obj.child()

# print()  # ----------------------------------------

# # (c) Multiple Inheritance
# class Father:
#     def skill1(self):
#         print("Father: Can drive")

# class Mother:
#     def skill2(self):
#         print("Mother: Can cook")

# class Son(Father, Mother):
#     def skill3(self):
#         print("Son: Can play guitar")

# obj = Son()
# obj.skill1()
# obj.skill2()
# obj.skill3()

# print()  # ----------------------------------------

# # (d) Hierarchical Inheritance
# class Parent:
#     def show(self):
#         print("This is Parent class")

# class Child1(Parent):
#     def child1(self):
#         print("This is Child 1 class")

# class Child2(Parent):
#     def child2(self):
#         print("This is Child 2 class")

# obj1 = Child1()
# obj2 = Child2()

# obj1.show()
# obj1.child1()

# obj2.show()
# obj2.child2()

# print()  # ----------------------------------------

# # (e) Hybrid Inheritance (combination)
# class A:
#     def showA(self):
#         print("Class A")

# class B(A):
#     def showB(self):
#         print("Class B")

# class C(A):
#     def showC(self):
#         print("Class C")

# class D(B, C):
#     def showD(self):
#         print("Class D (Hybrid Inheritance)")

# obj = D()
# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()

# print("\n All OOP Concepts Demonstrated Successfully!")


# # Encapsulation
# # Encapsulation is the process of bundling data (attributes) and methods (functions) that operate on that data into a single unit (class) and restricting direct access to some components for data protection.

# class Student:
#     def __init__(self, name, marks,n):
#         self.__name = name      # private variable
#         self.__marks = marks
#         self.n=n

#     def display(self):
#         print(f"Name: {self.__name}, Marks: {self.__marks}")

# s1 = Student("Tushar", 85,5)
# s1.__name="Riya"
# print(s1.n)
# s1.n=10
# print(s1.n)
# s1.display()
# # print(s1.__marks)
# # print(s1.__marks) ❌  --> Not accessible directly


# # Polymorphism
# # Polymorphism means same function name can have different behaviors depending on the object that calls it.

# class Cat:
#     def sound(self):
#         print("Meow")

# class Dog:
#     def sound(self):
#         print("Bark")

# c=Cat()
# c.sound()
# d=Dog()
# d.sound()
# # for animal in [Cat(), Dog()]:
# #     animal.sound()



# Abstraction
# Abstraction means hiding complex implementation details and showing only essential features to the user.

from abc import ABC, abstractmethod

# n=5

# print(n*n)

# sqn=0
# for i in range(n):
#     sqn=sqn+n
# print(sqn)

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started")

v = Car()
v.start()
