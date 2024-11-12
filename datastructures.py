"""

We will start of by defining a list. A list is a collection which is ordered and changeable. Allows duplicate members.
We will explore some methods for it 

"""

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")  # this will add orange to the list on last index
# thislist.insert(1, "blue")  # this will add blue to the list on index 1
# thislist.remove(
#     "banana"
# )  # Remove the first item from the list whose value is equal to banana. It raises a ValueError if there is no such item.
# thislist.pop()  # this will remove last item from the list
# thislist.pop(0)  # this will remove item from index 0
"""
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the 
last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.
"""
# thislist.clear()  # this will clear the list
# thislist.count("apple")  # this will count the number of items item appears in the list
# thislist.sort()  # this will sort the list
# thislist.reverse()  # this will reverse the list
# thislist.copy()  # this will copy the list
# print(thislist)


"""
Using Lists As Stacks 
The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). 
To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack,
use pop() without an explicit index. For example:

"""

# a = [1, 23, 54, 4, 6, 3]
#
# a.append(5)
# print(a)
# a.pop()
# print(a)
#
# print(a[-1])


"""

Using Lists As Queues
The list methods make it very easy to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”).
To add an item to the end of the queue, use append(). To retrieve an item from the beginning of the queue, use pop(0).
For example:


"""

# from collections import deque
#
# a = deque([1, 23, 54, 4, 6, 3])
# a.append(5)
# print(a)
# a.popleft()
# print(a)

"""

List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. 
For example, you can make a new list where each element is the result of some operations applied to each element of an existing list.

"""


# squares = []
#
# print(squares)
#
# for i in range(10):
#     squares.append(i**2)
# print(squares)
#
# """Or Even Better"""
#
# squares1 = list(map(lambda x: x**2, range(10)))
# print(squares1)


# squares = [x**2 for x in range(10)]
# print(squares)

"""Nested List Comprehension"""
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# transposed = [[row[i] for row in matrix] for i in range(3)]
# print(transposed)

"""There is a way to remove an item from a list given its index instead of its value: the del statement. 
This differs from the pop() method which returns a value. The del statement can also be used to remove slices from 
a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:"""


# thisList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# del thisList[0]
# print(thisList)


"""Tuples And Sequences
Tuples are similar to lists, but they are immutable. Tuples are created with the tuple() constructor or the built-in function tuple().
We saw that lists and strings have many common properties, such as indexing and slicing operations.
They are two examples of sequence data types (see Sequence Types — list, tuple, range). Since Python is an evolving language,
other sequence data types may be added. There is also another standard sequence data type: the tuple.
A tuple consists of a number of values separated by commas, for instance:
"""

# thisTuplle = "gyanesh", "kumar", "kumar", "kumar"
# print(thisTuplle)
# thisTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(thisTuple[0])


"""Sets In Python
Sets are another collection data type in Python. Like lists, sets are created with the set() constructor or the built-in function set().
We saw that lists and strings have many common properties, such as indexing and slicing operations.
They are two examples of sequence data types (see Sequence Types — list, tuple, range). Since Python is an evolving language,
other sequence data types may be added. There is also another standard sequence data type: the tuple.
A tuple consists of a number of values separated by commas, for instance:"""

# basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
#
# print(basket)
#
# if "orange" in basket:
#     print("Orange is a fruit")


"""Dictionaries : Another useful data type built into Python is the dictionary (see Mapping Types — dict).
Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”.
Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be 
any immutable type; strings and numbers can always be keys.
uples can be used as keys if they contain only strings, numbers, or tuples;
if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key
You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().
It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary).
A pair of braces creates an empty dictionary: {}.
"""


# tel = {"jack": 4098, "sape": 4139}
#
# print(tel["jack"])
# print(list(tel))


"""Looping Techniques in Python for dictionaries  """


knights = {"gallhad": "the pure", "robin": "the brave"}


for key, values in knights.items():
    print(key, values)
