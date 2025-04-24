from abc import abstractmethod
from typing import Any


#1 : Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
def display(self):
    print(self.name, self.marks)

person1 = Student("sdaddaw", 85)
display(person1)

#2 : Using cls
class Counter:
    count = 0

    def __init__(self, Amount) -> None:
        self.Amount = Amount
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

counter1 = Counter(10)
counter2 = Counter(20)
counter3 = Counter(30)

print(f"Total Counter objects created: {Counter.get_count()}")

#3 : Public Variables and Methods
class Car:
    def __init__(self, brand) -> None:
        self.brand = brand
    
    def Start(self) :
        print(f"The {self.brand} car's engine started.")

car1 = Car("Toyota")
car1.Start()

#4 : Class Variables and Class Methods
class Bank:
    def __init__(self, Bank_Name) -> None:
        self.bank_name = Bank_Name
    
    @classmethod
    def Change_Bank_Name(cls, name) :
        cls.bank_name = name
        print(cls.bank_name)

Bank1 = Bank("midani")
Bank1.Change_Bank_Name("Jmfdif")

#5 : Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
Add1 = MathUtils.add(21,45)
print(Add1)

#6 : Constructors and Destructors
class Logger:
    Count = 0
    def __init__(self, Amount) -> None:
        self.Amount = Amount
        Logger.Count += 1
        print(f"Logger object created with amount: {Amount}")
    
    def __del__(self):
        print(f"Logger object with amount {self.Amount} is being destroyed")

logger1 = Logger(100)
logger2 = Logger(200)
logger3 = Logger(300)
        
print(f"Total Logger objects created: {Logger.Count}")

#7 : Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, _salary, __ssn) -> None:
        self.name = name
        self._salary = _salary
        self.__ssn = __ssn
    
employee1 = Employee("dwdadwww", 31234, 3341)
print(employee1.name)
print(employee1._salary)
# print(employee1.__ssn)       AttributeError: 'Employee' object has no attribute '__ssn'

#8 : The super() Function
class Person:
    def __init__(self, name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject

teacher = Teacher("John Smith", "Mathematics")
print(f"Teacher: {teacher.name}, Subject: {teacher.subject}")

#9 : Abstract Classes and Methods
class Rectangle:
    def __init__(self, Side1To3, Side2To4) -> None:
        self.Side1_3 = Side1To3
        self.Side2_4 = Side2To4

class Shape(Rectangle):
    
    @abstractmethod
    def area(self):
        print(self.Side1_3 * self.Side2_4)

#10 : Instance Methods
class Dog:
    def __init__(self, name, breed) -> None:
        self.name = name
        self.breed = breed
    
    def bark(self) :
        print(f"{self.name} says Woof!")

#11 : Class Methods
class Book:
    total_books = 0
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
    def __init__(self):
        Book.increment_book_count()

book1 = Book()
book2 = Book()
print(f"Total Books: {Book.total_books}")

#12 : Static Methods
class TemperatureConvertor:    

    @staticmethod
    def Celcius_To_Farenheit(celsius):
        Farenheit = (celsius * 9/5) + 32 
        print(f"{Farenheit} F")

    def __init__(self, Celsius) -> None:
        self.celcius = Celsius
        self.Celcius_To_Farenheit(self.celcius)

celc = TemperatureConvertor(0)

#13 : Composition
class Engine:
    def __init__(self, cylinders, displacement) -> None:
        self.cylinders = cylinders
        self.displacement = displacement
    
    def get_engine_specs(self):
        return f"{self.cylinders} cylinders, {self.displacement}L"

class Car:
    def __init__(self, brand, model, engine) -> None:
        self.brand = brand
        self.model = model
        self.engine = engine
    
    def display_specs(self):
        print(f"{self.brand} {self.model} with {self.engine.get_engine_specs()}")

#14 : Aggregation
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def get_info(self):
        return f"Employee: {self.name} (ID: {self.employee_id})"

class Department:
    def __init__(self, name, employee=None):
        self.name = name
        self.employee = employee
    
    def set_employee(self, employee):
        self.employee = employee
    
    def get_department_info(self):
        if self.employee:
            return f"Department: {self.name} - {self.employee.get_info()}"
        return f"Department: {self.name} - No employee assigned"
    
#15 : Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("Show A")

class B(A):
    def show(self):
        print("Show B")

class C(A):
    def show(self):
        print("Show C")

class D(B, C):
    def show(self):
        super().show()

d = D()
d.show()

#16 : Function Decorators
def Log_Functional_Call(Func):
    print("Function is being called")
    Func()

@Log_Functional_Call
def Say_Hello():
    print("Hello World")

#17 : Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self):
        pass

#18 : Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, _price) -> None:
        self._price = _price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price
    
#19 : callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, input):
        return input * self.factor
    
    print(callable(__call__))

multiply_by_5 = Multiplier(5)
print(callable(multiply_by_5))  
print(multiply_by_5(10))     

#20 : Creating a Custom Exception
class InvalidAgeError:
    def __init__(self, Message, Error_Code) -> None:
        super().__init__(Message)
        self.error_code = Error_Code
    
    def __str__(self) -> str:
        return "Invalid Age"

def CheckAge(Age):
    if Age < 18:
        raise InvalidAgeError
    else :
        print("Hello world")

Age = 19
CheckAge(Age)

#21 : Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for i in Countdown(214):
    print(i)