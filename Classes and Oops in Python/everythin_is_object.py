# Defining a simple class
class Dog:
    def bark(self):
        return "Woof!"

# Creating an instance of the Dog class
my_dog = Dog()

# Checking the type of the instance
print(type(my_dog))  # Output: <class '__main__.Dog'>

# Checking the type of the class itself
print(type(Dog))  # Output: <class 'type'> it is a meta class
# Using methods on fundamental data types
num = 10
print(num.bit_length())  # Output: 4 (number of bits needed to represent 10)

text = "Hello"
print(text.upper())  # Output: "HELLO"
def greet():
    return "Hello, World!"

# Assigning the function to a variable
greeting = greet
print(greeting())  # Output: "Hello, World!"
