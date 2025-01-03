"""
if you want to write a somewhat longer program, you are better off using a text editor to prepare 
the input for the interpreter and running it with that file as input instead. This is known as creating a script. As your program 
gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy
function that you’ve written in several programs without copying its definition into each program.
To support this, Python has a way to put definitions in a file and use them in
a script or in an interactive instance of the interpreter. Such a file is called a module;
definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in
a script executed at the top level and in calculator mode).
A module is a file containing Python definitions and statements.
The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available
as the value of the global variable __name__.
"""


def fibo(x):
    a, b = 0, 1
    while a < x:
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    import sys

    fibo(int(sys.argv[1]))  # This Will take The First Argument As Input

"""And Now If I open python interpreter on My command Line And Type 'import modules.py' Then i will be able to use fibo function """
