Python notes from Youtube Tutorial "Python Tutorial for Programmers - Python Crash Course" by 
Programming with Mosh.


TOOLS -

Editor - program to write your code in. Examples include VSCode, Atom, Sublime and many others. You can add extensions
to the editor to act as an IDE, for example Linting, Unit Testing, debugger, code formatting ect.


IDE - Integrated Development Environment; code editor with autocompletion, testing and debugging capabilities.
Examples include PyCharm for Python.

Always update editor to latest version and add pylint so that it can let you know potential errors and mistakes in your code.

Python PEPs (Python Enhancent Proposals)

most popular PEP is number 8 in the Python documentation (python.org/dev/peps/)
it is a guide for how to to style/format Python code. This allows for consistency in your code.

Code Runner extension, cool extension for not having to
go to terminal and run code all the time.

ctrl+alt+n

Python Implementation - program that understands Python rules and runs the code
eg CPython program written in C language.
others are 
Jython - java
IronPython - C#
PyPy - subset of Python
theoretically, if you give any python code to run under these implementations, one
should get the same results

Execution of Python code - 
Python code goes through a compiler called CPython which then gets turned into Python 
Bytecode, then this Bytecode passes thorugh the Python Virtual Machine to then 
covert it into Machine code and execute it.

Typing - 
Static languages - c++ c# java

when declaring a variable, we need to specify the type of variable
e.g

c# int students = 100
this is always set to an integer

Dynamic languages - js, ruby, python 

no need to set a type, just set variable to a value.
However if you ever need to know the type of variable in a dynamic language
such as Python we can use the following code

print(type(variable name here)) and in the console it should give you
the type of variable it is.

difference between dynamic variable types and static variable types, is
that in a dynamic language the variable type is determined at run time
rather than during the compiling type such as in a static language lik java.

Type Annotation - 

lines 47-53 on file app.py

Built in Function id(variable name here) will let you know the memory location of the stored varible.
Mutable types give you a different storage location while inmutable types stay at the same storage location.

lines  57-66  on file app.py

Strings - 

lines 68-91 on file app.py

Escape Sequences - 

lines 93-103 on file app.py

Formatted Strings  - 

lines 107-114 on file app.py

String Methods - 

lines 116-135 on file app.py

Numbers - 

to represent numbers we can use decimals, binary format, then add individual bits.

lines 137-156 on file app.py

ARITHMETIC OPERATIONS - 

There is not increment or decrement methods eg
x++ or x--

lines 159-183 on file app.py

Numbers continued - 

google built-in functions in python to learn all about them.

lines 186-196 on file app.py


Math Modules - 

import the math module at the top of the file
for more information google python 3 math module

lines 186-196 on file app.py

TYPE CONVERSIONS - 

lines 186-196 on file app.py

Falsy
"" empty strings
0
[] empty arrays or lists
none (null)

print(bool(x)) false, anything else is true

CONDITIONAL STATEMENTS - 

lines 213-226 on file app.py

LOGICAL OPERATORS - 
and 
or
not

lines 228-251 on file app.py

 Ternary Operator - 


lines 228-251 on file app.py










