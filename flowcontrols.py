"""Input is the function which is used to take user input from the command line And  By Default it takes input as string"""

# takeInput = input("Enter Your Name: ")
# print("Hello " + takeInput)
# print(type(takeInput))

"""How TO Take input as a user and convert it into integer"""

# takeInput = int(input("Enter Your Age: "))
# print(type(takeInput))

# if takeInput % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
"""
Lets Take an Example of if else statement We Will Make A function Which takes age of the user as input and 
returns whether the person is eligible for voting or not.
if the age is odd then person will be sent to camp a or else b 
"""

#
# def checkAge(age):
#     if age <= 0 | age > 150:
#         print("Please Enter The Valid Age")
#     elif age < 18:
#         print("You Are Not Eligible For Voting")
#     elif age >= 18:
#         print("You Are Eligible For Voting")
#         if age % 2 == 0:
#             print("You are given camp a for voting")
#         else:
#             print("You are given camp b for voting")
#
#
# def main():
#     while True:
#         try:
#             x = int(input("Enter Your Age: "))
#             checkAge(x)
#             break
#         except ValueError:
#             print("Please Enter The Valid Age")
#
#
# if __name__ == "__main__":
#     main()


"""
For Statement in Python The for statement in Python differs a bit from what you may be used to in C or Pascal.
Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the
ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence 
(a list or a string), in the order that they appear in the sequence. For example (no pun intended) 

"""

# words = ["bat", "cat", "rat"]
#
# for w in words:
#     print(w, len(w))
#

"""

The Range functions 

If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:

The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10.

"""
# a = list(range(5))
# print(a)


"""

Break Statement In Python
The break statement in Python terminates the innermost enclosing for or while loop. 
It causes the control to transfer to the statement immediately following the loop.

"""

"""Continue Statement In Python
The continue statement in Python is used to skip the rest of the code inside a loop for the current iteration only. 
It causes the control to transfer to the start of the for or while loop.
"""

"""
Pass Statement In Python
The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
"""


"""

Match Statement In Python
The match statement in Python is used to perform pattern matching on a value. 
It is a convenient way to check if a value matches a pattern.

"""

#
# def http(status_code):
#     match status_code:
#         case 200:
#             print("OK")
#         case 404:
#             print("Not Found")
#         case 500:
#             print("Internal Server Error")
#         case _:
#             print("Unknown Status Code")


# def fibb(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         a, b = b, a + b
#
#
# fibb(2000)


"""
Function In Python
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

"""


def function_name(parameter1, parameter2):
    # Function body
    return True


"""

Types of Parameters:


Regular parameters: def greet(name)
Default parameters: def greet(name="User")
*args: for variable number of positional arguments
**kwargs: for variable number of keyword arguments

Example:

"""


def greet(name, age=20, *hobbies, **details):
    print(f"Hi {name}, age {age}")
    print("Hobbies:", hobbies)
    print("Additional details:", details)


greet("Alice", 25, "reading", "gaming", city="New York", job="developer")

"""
Return Values:
"""


def add(a, b):
    return a + b  # Returns one value


def stats(numbers):
    return min(numbers), max(numbers)  # Returns multiple values as tuple


"""

Lambda Functions:

A lambda function is a small anonymous function. 
A lambda function can take any number of arguments, but can only have one expression.
Lambda Functions (anonymous one-line functions):
"""

square = lambda x: x**2
