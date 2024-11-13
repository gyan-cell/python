"""Classes Creating a new class creates a new type of object, allowing new instances of that type to be made.
Each class instance can have attributes attached to it for maintaining its state.
Class instances can also have methods (defined by its class) for modifying its state.   
 Objects can contain arbitrary amounts and kinds of data. As is true for modules, 
 classes partake of the dynamic nature of Python:
 they are created at runtime, and can be modified further after creation.
"""

"""
Although scopes are determined statically, they are used dynamically. At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:

    the innermost scope, which is searched first, contains the local names

    the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contain non-local, but also non-global names

    the next-to-last scope contains the current module’s global names

    the outermost scope (searched last) is the namespace containing built-in names
"""


# def scope_test():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
#
# scope_test()
# print("In global scope:", spam)


# class myClass:
#     i = 67256
#
#     def f(self):
#         return "hello world"
#
#
# x = myClass()
# print(x.i, x.f())


# class Dog:
#     kind = "Canine"
#
#     def __init__(self, name) -> None:
#         self.name = name
#
#
# d = Dog("Fido")
# e = Dog("Buddy")
# print(d.name, d.kind)
# print(e.name, e.kind)

# this is a bad design
# class Dog:
#     trick = []
#
#     def __init__(self, name) -> None:
#         self.name = name
#
#     def add_trick(self, trick):
#         self.trick.append(trick)
#
#
# d = Dog("Fido")
# e = Dog("Buddy")
# d.add_trick("roll over")
# e.add_trick("play dead")
# print(d.name, d.trick)
# print(e.name, e.trick)


# class Dog:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.tricks = []
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
#
#
# d = Dog("Fido")
# e = Dog("Buddy")
# d.add_trick("roll over")
# e.add_trick("play dead")
# print(d.name, d.tricks)
# print(e.name, e.tricks)
#
#
#


class tarinTicket:
    def __init__(self, name, ticketQty, address, price) -> None:
        self.name = name
        self.ticketQty = ticketQty
        self.address = address
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} {self.ticketQty} {self.address} {self.price}"

    def details(self) -> str:
        return f"{self.name} {self.ticketQty} {self.address} {self.price}"


train = tarinTicket("Rajdhani Express", 10, "Delhi", 1000)
print(tarinTicket)
print(train)
