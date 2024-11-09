"""Numbers In Python"""


a=876
#here a and b are the variables and equato sign is used to assign values
b=10
# This will add two numbers
print(a+b)
# This will subtract two Numbers
print(a-b)
# This will multiply two Numbers
print(a*b)
# This will divide two Numbers and returns a floating point number which happens to be the quotient
print(a/b)
# This will return the remainder
print(a%b)
# This will return the integer division
print(a//b)
# This will return the power
print(a**b)


"""Python can manipulate text (represented by type str, so-called “strings”) as well as numbers. 
This includes characters “!”, words “rabbit”, names “Paris”, sentences “Got your back.”, etc. “Yay! :)”.
They can be enclosed in single quotes ('...') or double quotes ("...") with the same result ."""


string  = "Yay! :) , 'Yes', they said.'"
print("""\

Usage: thingy [OPTIONS]

     -h                        Display this usage message

     -H hostname               Hostname to connect to

""")


print(string)
"Strings can be concatenated (glued together) with the + operator, and repeated with *:"
print("Hello" + "World")
print("Hello" * 3)
print(3 * 'un' + 'ium')


"""Strings can be indexed (subscripted), with the first character having index 0. 
There is no separate character type; a character is simply a string of size one:"""

word = 'Python'
print(word[0])  # print 'P'
print(word[5])  # print 'n'
print(word[-1])  # print 'n'
print(word[-2])  # print 'o'
print(word[-6])  # print 'P'
