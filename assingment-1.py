"""Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details. """

"""Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details. """

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Example usage:
s1 = Student("Alice", 92)
s1.display()

"""Assignment:2
Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count."""

class Counter:
    # Class variable (shared by all objects)
    count = 0

    def __init__(self):
        # Jab bhi naya object banta hai, count barh jata hai
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print("Total objects created:", cls.count)

# Ab kuch objects banate hain
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Ab class method call karte hain
Counter.display_count()


"""3. Public Variables and Methods
Assignment:3
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

"""
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"{self.brand} is starting.")
# Example usage:
my_car = Car("Toyota")
print(my_car.brand)  # Accessing public variable
my_car.start()  # Calling public method
