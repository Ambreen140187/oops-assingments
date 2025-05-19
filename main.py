"""4. Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

"""
class Bank:
    # Class variable
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Change the class variable
# Example usage:
bank1 = Bank()
    

bank2 = Bank()
print("Initial Bank Name:", bank1.bank_name)  # Output: Default Bank


"""Assignment:5
Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

"""
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b  # Static method that adds two numbers
# Example usage:
result = MathUtils.add(5, 3)    
print("Sum:", result)  # Output: Sum: 8

"""Assignment:6     
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

"""
class Logger:
    def __init__(self):
        print("Object created.")

    def __del__(self):
        print("Object destroyed.")
# Example usage:
obj = Logger()  # This will print "Object created."
del obj  # This will print "Object destroyed." (when the object is deleted)

"""Assignment:7
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.

"""
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable
# Example usage:
emp = Employee("John Doe", 50000, "123-45-6789")    

print("Name:", emp.name)  # Accessing public variable
print("Salary:", emp._salary)  # Accessing protected variable (not recommended
# but possible)
# print("SSN:", emp.__ssn)  # This will raise an AttributeError because __ssn is private

"""Assignment:8
Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

"""
class Person:
    def __init__(self, name):
        self.name = name  # Constructor that sets the name
# Example usage:
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the base class constructor   

        self.subject = subject  # Add a subject field
# Example usage:
teacher = Teacher("Alice", "Mathematics")
print("Name:", teacher.name)  # Accessing name from base class
print("Subject:", teacher.subject)  # Accessing subject from derived class

"""Assignment:9
Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

"""
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method
# Example usage:
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Implementing the abstract method
# Example usage:
rect = Rectangle(5, 10)
print("Area of Rectangle:", rect.area())  # Output: Area of Rectangle: 50


"""Assignment:10
Assignment:
Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

"""
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable

    def bark(self):
        print(f"{self.breed} says Woof!")  # Instance method that prints a message       
# Example usage:
dog = Dog("Buddy", "Golden Retriever")
dog.bark()  # Output: Buddy says Woof


"""Assignment:11

Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

"""
class Book:
    total_books = 0  # Class variable

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increment the class variable
# Example usage:
book1 = Book()
Book.increment_book_count()  # Increment the count
book2 = Book()
Book.increment_book_count()  # Increment the count
print("Total books:", Book.total_books)  # Output: Total books: 2

"""Assignment:12
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

"""
"""Assignment:12
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

"""
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32  # Static method to convert Celsius to Fahrenheit

# Example usage:
temp_in_celsius = 25
temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_in_celsius)
print(f"{temp_in_celsius}°C is {temp_in_fahrenheit}°F")  # Output: 25°C is 77.0°F

"""Assignment:13
Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

"""
class Engine:
    def start(self):
        print("Engine started.")  # Method of Engine class  
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine object

    def start(self):
        self.engine.start()  # Accessing method of Engine class via Car class
# Example usage:
engine = Engine()  # Creating an Engine object  
car = Car(engine)  # Passing Engine object to Car class
car.start()  # Output: Engine started.

"""Assignment:14
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.



"""
class Department:
    def __init__(self, name):
        self.name = name  # Department name

    def show_department(self):
        print(f"Department: {self.name}")  # Method to show department name
class Employee:
    def __init__(self, name, department):
        self.name = name  # Employee name
        self.department = department  # Aggregation: Employee has a reference to Department

    def show_employee(self):
        print(f"Employee: {self.name}")
        self.department.show_department()  # Accessing method of Department class
# Example usage:
department = Department("HR")  # Creating a Department object
employee = Employee("Alice", department)  # Passing Department object to Employee class

employee.show_employee()  # Output: Employee: Alice, Department: HR

"""Assignment:15
Method Resolution Order (MRO) and Diamond Inheritance
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.

"""
class A:
    def show(self):
        print("Class A")  # Method of class A

class B(A):
    def show(self):
        print("Class B")  # Overriding method in class B
class C(A):
    def show(self):
        print("Class C")  # Overriding method in class C    
class D(B, C):
    def show(self):
        print("Class D")  # Overriding method in class D    
# Example usage:
d = D()  # Creating an object of class D
d.show()  # Output: Class D
# MRO
print("MRO:", D.__mro__)  # Output: MRO: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# This shows the order in which classes are searched when calling a method.
# In this case, D inherits from B and C, and the method resolution order is D -> B -> C -> A.

# This means that if a method is not found in D, it will look in B first, then C, and finally A.
# This is an example of the diamond problem, where a class inherits from two classes that have a common ancestor.



# The MRO ensures that the method resolution is done in a consistent order, avoiding ambiguity.
# The diamond problem occurs when a class inherits from two classes that have a common ancestor, leading to ambiguity in method resolution.

# The MRO ensures that the method resolution is done in a consistent order, avoiding ambiguity.


    

"""Assignment:16
Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().
"""

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello, World!")

# Example usage:
say_hello()  # Output: Function is being called, Hello, World!
"""Assignment:17
Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

"""
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"  # Method added by the decorator
    cls.greet = greet  # Adding the method to the class
    return cls
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage:
person = Person("Alice")


print(person.greet())  # Output: Hello from Decorator!
"""Assignment:18
Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

"""
class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price  # Getter method

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = new_price  # Setter method

    @price.deleter
    def price(self):
        del self._price  # Deleter method

# Example usage:
product = Product(100)
print("Initial Price:", product.price)  # Output: Initial Price: 100
product.price = 150  # Updating the price
print("Updated Price:", product.price)  # Output: Updated Price: 150
del product.price  # Deleting the price
# print(product.price)  # This will raise an AttributeError because the price has been deleted

"""Assignment:19
Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

"""
class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Setting the factor

    def __call__(self, x):
        return x * self.factor  # Multiplying input by the factor
# Example usage:
multiplier = Multiplier(3)  # Creating an object with factor 3
print(callable(multiplier))  # Output: True (multiplier is callable)
result = multiplier(5)  # Calling the object like a function
print("Result:", result)  # Output: Result: 15

"""Assignment:20
Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

"""
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass    
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")  # Raising custom exception
# Example usage:


try:

    check_age(15)  # This will raise InvalidAgeError
except InvalidAgeError as e:
    print("Caught an exception:", e)

"""Assignment:21
Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

"""
class Countdown:
    def __init__(self, start):
        self.current = start  # Setting the start number

    def __iter__(self):
        return self  # Returning the iterator object

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop iteration when current is less than 0
        else:
            current_value = self.current
            self.current -= 1  # Decrementing the current value
            return current_value  # Returning the current value
# Example usage:
countdown = Countdown(5)  # Creating a Countdown object starting from 5
for number in countdown:
    print(number)  # Output: 5, 4, 3, 2, 1, 0





 



        

