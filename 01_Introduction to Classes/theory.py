"""

Introduction to Classes
Types

Python equips us with many different ways to store data. A float is a different kind of number from an int, and we store
different data in a list than we do in a dict. These are known as different types. We can check the type of a Python
variable using the type() function.
"""

a_string = "Cool String"
an_int = 12

print(type(a_string))
# prints "<class 'str'>"

print(type(an_int))
# prints "<class 'int'>"

"""
Above, we defined two variables, and checked the type of these two variables. A variable’s type determines what you can
do with it and how you can use it. You can’t .get() something from an integer, just as you can’t add two dictionaries
together using +. This is because those operations are defined at the type level.
Instructions
1.

Call type() on the integer 5 and print the results.

You can call type() on anything. Like this dictionary!

type({'abc': True})

Print the results!
2.

Define a dictionary my_dict.
3.

Print out the type() of my_dict.
4.

Define a list called my_list.
5.

Print out the type() of my_list.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
