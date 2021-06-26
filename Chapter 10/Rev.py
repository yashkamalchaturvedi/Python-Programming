# Visual Studio Code 
# It is a source-code editor or IDE developed by Microsoft for all major OS’s. 
# It have features like debugging, embedded Git control and GitHub, syntax highlighting, intelligent code completion, snippets, and code refactoring. 
# There are a lot of features in VS Code which make it one of most favorite code editor among coders. Features like:
# Multiple terminals running at the same time
# Multiple files open at the same time which is awesome for web developers
# We can install various extensions in it
# We can install different python interpreters and change according to our need
# Multiple cursor points to edit or write repeating text
# There is a bar named “outline” in which all modules, classes, functions, variables and everything is listed in an organized way with their own logos making it very easy to differentiate and access.
# It gives you an overview of your code in a minimized way.

# Programming Languages :
# Programming Language are the languages which allows users to interact with computer and these languages comprises of set of instructions which produce various kinds of outputs.
# Programming Languages are used to create programs which allow users to perform complex task in seconds.
# Programming Languages are used because computer doesn’t understand human languages so we write code in programming language which later on get converted by language processors in machine language or binary code.

# Python in Brief :
# Python is a high-level, general-purpose programming language. Python use interpreter as its language processor.
# Python is used to develop GUI Programs, Web Applications, websites, Games, scripts, etc. and python is even used in networking and all. Python is even used to do photo editing, video editing and other type of general purpose work.
# This programming language is used mostly everywhere in tech field. It is used in Data Science, AI, Machine learning etc. 

# Python in Power Shell :
# We can write code in Power Shell of windows. But the problem is that it’s like interactive mode i.e. we can only write one line code at a time and then we have to execute it. 
# So, this type of interactive mode is used when we want to check any error in any specific line or at the time of debugging the program.
# So, we should write code in good IDE i.e. VS Code. Because it provide us many features and allows us to write good and efficient code.

# print("Hello world")
# In this code we wrote a function (print) which allows us to print anything which is written inside that function in double quotes (“”).
# So, in print function when we use “” (Double Quotes) it means anything enclosed in double quotes will be displayed as it is and is known as string.
# String is a data type in Python which is related to text. And to make string just enclose that part in either (‘’) Single or (“”) Double quotes.

# Comments in Python :
# Comments are the code which is not executed while interpreting the code. Comments are used to make the code more understandable for the programmer. 
# There are two types of comments in Python :-
# Single Line Comments
# Multi-Line Comments
# Single Line comment is the comments which are created in single line only i.e. they occupy the space of single line only.
# These are created using # (Hash/Pound Symbol) in Python.
# Multi Line comment are the comments which are created by using multiple lines i.e. they occupy more than one line in the program.
# These are created using triple quote (‘’’ Comment Code ‘’’) in Python.

# '''
# This is a multi line comment
# '''
# This is a comment

# print(5+8) # 13
# print(5+8) # 5+8

# Indentation in Python :
# There are 3 types of statements in Python :-
# Simple Statement
# Empty Statement
# Complex Statement
# In Complex statements there are two portions, header and body.

# if (5>4): #This is the header part
#     print("5 is greater than 4") #This is body part
#     print("Got it!")
# else:  #This is the header part
#     print("Bye guys!")  #This is body part

# So, indentation means leaving a TAB space from margin and in python it is used to show that statements which are indented belong to upper statement.
# In statements like if, if-else, elif, for etc. we use indentation because these all are type of complex statements and they have two parts as I already told you header and body.
# We have to indent our body statements to show that these are sub-statements of our main statements which is written in header portion.

# Module – Module or library is the file which contain definitions of several functions, classes, variables, etc. which are written by someone else for free use.
# Modules are used in code when we want to do some work and that work is already done by someone else and available in any module then we can simply import that module and can use that code in our program.
# There are many modules in Python which can be downloaded from internet and can be used in our python program.
# And there are some built-in modules also which are available to use when we are offline.

# import math #Here we have imported a built-in module 'math'
# print("Here we will use some math functions")
# a = 2
# b = 4
# c = math.sqrt(16)
# d = math.pow(a,b)
# print(c)
# print(d)

# So, in above code as you can see we have downloaded a module named as open cv-python. So that’s how you can download module :
# #pip install __module__name
# And After downloading modules you have to simple import them or use them in your program.
# So, to do so simply type:  import _module_name  in your code.
# That’s how you can use module in your programs.

# A variable is a name or an identifier which is given to any storage area or memory location.
# It’s a name of memory location.
# Rules for defining a variable in Python :-
# Variable name can contain alphabets, digits, and underscore (_).
# Variable name can start with an alphabet and underscore only.
# It can’t start with a digit.
# No whitespace and reserved keywords are allowed to use as a variable name.
# Variables are case-sensitive.
# E.g. a=5, _demo = “Name”, De_mo1 = 65.85, etc.

# Type-Casting :
# Type-casting is defined as converting one data type into another for smooth functioning of program.
# With type() function we can find the type of any variable.
# print("\t\tType Casting")
# a = 52
# b = 58.68
# c = "Demo"
# print(type(a))
# print(type(b))
# print(type(c))

# Type-casting is done when we want to perform arithmetic operations on the variables of same data type.
# print("\t\tType Casting\n")
# a = 15
# b = "25"
# print(type(b))
# b = int(b)
# print(type(b) )
# print("Sum of a and b is",a+b)

# Strings :
# String literal in python are enclosed in either single quotes (‘’) or double quotes (“”).
# It means “hello” is same as ‘hello’.
# We can simply assign string to a variable.

# print("\t\t Strings")
# a = "Hello"
# print(a)
# demo = '''
# This is an
# example of
# multi-line
# string.
# '''
# print((b))

# So, here we declared a variable Demo and in that variable we assigned a multi-line string.
# In multi-line strings also we can use either single quotation mark or double quotation mark.

# String Slicing :
# In Python to use any specific character of string we use index no.
# Index no. is a special type of no. which allows us to extract any character from string.
# Index no. starts from 0.

# For example:
# print("\t\t Strings")
# a = "Hello"
# print(a[0])
# print(a[1])
# print(a[2:5])

# String Functions :

# variable_name.strip() = This function allows us to remove all the blank spaces near to string.
# print("\t\t Strings")
# a = "   Hello  "
# print(a)
# print(a.strip())

# len() = len function counts the total characters of any string.
# print("\t\t Strings")
# a = "Hello"
# print(a)
# print(len(a))

# variable_name.lower() = This function converts all the characters in lower case of a string.
# print("\t\t Strings")
# a = "Hello"
# print(a)
# print("\n")
# print(a.lower())

# variable_name.upper() = This function converts all the characters in upper case of a string.
# print("\t\t Strings")
# a = "Hello"
# print(a)
# print("\n")
# print(a.upper())

# variable_name.replace(“char1”, ”char2”) = This function replaces char1 by char2 in a string.
# print("\t\t Strings")
# a = "Hello"
# print(a)
# print(a.replace('ello', 'i'))

# Adding Strings :
# We can simply add two or more strings by using ‘+’ operator between two variables.
# print("\t\t Strings")
# a = "Hello"
# b = " Guys"
# print(a+b)

# Format Strings :
# It means we can easily format string by using .format function.
# print("\t\t Strings")
# a = "Demo"
# b = "Format"
# print("This is the {} string".format(a,b))
# print("This is the {0} string".format(a,b))
# print("This is the {1} string".format(a,b))

# In placeholders we can pass values such as 0,1 etc.
# print("\t\t Strings")
# a = "Demo"
# b = "Format"
# print(f"This is a {a} of {b} string")

# Operators :
# An Operator is a symbol which is used to perform operations on operands in any programming language.
# In python there are many type of operators :
# ** - This is an exponential operator i.e. if we write 2**3 then it means 2 raise to power 3.
# // ( Floor division ) – This divides two no. but returns a integer value.
# % (Modulus Operator) – This operator returns the remainder.
# There are many more operators such as +,-,*,/ etc.

# Lists :
# A List in Python represents a list of comma-separated values of any data type between square brackets.
# print("\t\tList\n")
# lst = [8,5,2,9,7]
# print(lst)
# print(type(lst))
# print(lst[0])
# print(lst[1])
# print(lst[2: 5])

# List Functions :

# variable_name(list).append – This function adds a new value or element in the end of the list.
# lst = [8,5,2,9,7]
# print(lst)
# print(type(lst))
# lst.append(99)      
# print(lst)

# variable_name(list).insert(index_no, value) – This function adds a new element at any index no. in the list.
# lst = [8,5,2,9,7]
# print(lst)
# print(type(lst))
# lst.insert(0,99)        
# print(lst)

# variable(list).remove(element) – This function removes an element from the list.
# lst = [8,5,2,9,7]
# print(lst)
# print(type(lst))
# lst.remove(2)       
# print(lst)

# variable(list).pop() – This function removes one element from the end of the list.
# lst = [8,5,2,9,7]
# print(lst)
# print(type(lst))
# lst.pop()       #remove one element from list
# print(lst)

# del variable[index_no] – This keywords allows us to remove or delete any particular element from the list by using it’s index no.
# lst = [8,5,2,9,7]
# print(lst)
# print(type(lst))
# del lst[2]       #remove the element at index 2
# print(lst)
# del variable(list) – This is used to delete whole list from the program.

# Variable(list).clear – This function removes all the elements of the list.
# lst = [8,5,2,9,7]
# print(lst)
# print(type(lst))
# lst.clear()       #clears the list
# print(lst)

# Tuples:
# These are those lists which cannot be changed i.e., are not modifiable. 
# Tuples are represented as list of comma-separated values of any date type within parentheses.
# Tuples doesn’t allow modification.
# If we wish to modify any tuple then we’ll get error but we can modify type after converting or type casting it into the list.
# print("\t\tTuples\n")
# tup = ('Demo', 'Hello', 54, 'Guys')
# print(tup)
# print(type(tup))
# tup = list(tup)
# tup[1] = 99
# print(tup)

# Sets :
# Sets in python are a data type equivalent to sets in mathematics. 
# It may consist various elements and the order is undefined.
# Sets elements are enclosed in {} Curly Braces.
# In sets repeated elements does not get printed.

# Sets Functions :

# variable_name.add(element ) – This function is used to add one element in the Set.
# print("\t\tSets\n")
# set1 = {1,2,3,4,5,1,2,3}
# print(set1)
# print(type(set1))
# set1.add(99)
# print(set1)

# variable_name.update([element1, 2, 3…]) – This function allows us to add many elements in the set.
# print("\t\tSets\n")
# set1 = {1,2,3,4,5,1,2,3}
# print(set1)
# print(type(set1))
# set1.update([5,6,99,109,199])
# print(set1)

# There are many more functions of sets such as .pop, .clear, del etc. Try them in your computer.

# Dictionary :
# Dictionary data type is another feature in Python's hat. The dictionary is an unordered set of comma-separated key: value pairs, within {},with the requirement that within a dictionary, no two keys can be the same (i.e., there are unique keys within a dictionary).
# print("\t\tDictionary\n")
# dictionary1 = {
#     "Play" : "Doing some activity",
#     "Food" : "Something eatable",
#     "Python" : "Language",
# }
# print(dictionary1)
# print(len(dictionary1))
# Dictionary Functions are same as of list, tuples etc. 

# In Python we can take input from user by using function:
# input()
# This function takes the input from user but it always take input in string data type i.e. if we want any arithmetic operation to be done on that input then we need to type cast that input into either int or float data type.
# print("\t Input statement \n")
# a = int(input("Enter any number: "))
# name = int(input("Enter any name: "))
# print(type(a))
# print(a)
# print(type(name))
# print(name)

# Conditional Statements :
# These are complex statements which possess some conditions. It means in these statements control only enters when the condition is true.
# So, In conditional statements we have 3 type of statements :
# if statement
# if-else statement
# elif statement

# if statement – In if statement condition is checked and if the condition is true then body of if statement get executed.
# print("\t Conditional Statements \n")
# x = int(input("Enter any number: "))
# if (x>100):
#     print("Number entered is greater than 100")
# print("END!")

# if-else statement – In if-else statements condition is checked and if condition is true then block of if statement get executed but if ‘if’ condition is false then block of else statement get executed.
# print("\t Conditional Statements \n")
# age = int(input("Enter your age: ")
# if (age>=18):
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# elif statement – In these type of statements, there are many instances when there is a need to check condition. 
# We use these statements when we have to check many conditions.
# print("\t Conditional Statements \n")
# x = int(input("Enter any number: ")
# if (x>50):
#     print("Number is greater than 50")
# elif (x>25):
#     print("No. entered is b/w 25-50")
# elif (x>0):
#     print("Number entered is between 0-25")
# else:
#     print("Enter valid number")

# Loops :
# Loops or iterative statements are the statements which allow repetition of block of code again and again till the condition become false.
# There are 2 type of loops in Python :
# for Loop and while loop.
# print("\t Loops \n")
# num = 5
# for a in range(1, 11 ):
#     print(num, 'x ', a, '=', num* a)
# print("\t Loops \n")
# x = 1
# while(x<=100):      #while loop
#     print(x)
#     x = x+1

# In loops sometimes we use break and continues statements :
# break statement is used to stop the loop before it has loops through all the items or statements.
# continue statement allows us to stop the current or active iteration of the loop and continue with the next iteration.

# Functions :
# A function is a block of codes that take inputs, do some specific task and produces output. We create functions when we have to do some work again and again in a program. That’s why we create function and calls it whenever we want to use it in our program.
# Creating a function :
# '''
# def function_name () :
#          statement 1,
#          statement 2,
#          ….
# '''

# print("\t Functions \n")
# def demo():     #Defining a function
#     print("Hlo Guys")
#     print("It's my First Function")
#     print(" : )")
# demo()      # Calling a function
# print("\t Functions \n")
# def add(a,b):        #Defining Function
#     c = a+b
#     return c
# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# z = add(x,y)        #Calling Function
# print("The Sum is", z)

# Object-Oriented Programming In Python
# Python is a multi-paradigm programming language. It has support for various approaches to problem-solving.
# OOP is one of the most popular and widely used approaches for problem-solving. In this approach, everything is treated as an object.
# The concept of OOP is mainly based on DRY, which means Do not repeat yourself.
# The main purpose of OOP is creating reusable code.
# OOP is associated with various concepts such as class, object, abstraction, encapsulation, inheritance etc.

# class Employee:
#     def __init__(self, gname, gsalary):
#         self.name = gname
#         self.salary = gsalary
# harry = Employee("harry", 34)
# print(harry.name)
# print(harry.salary)
