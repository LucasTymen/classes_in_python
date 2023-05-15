"""

Introduction to Classes
Class Variables

When we want the same data to be available to every instance of a class we use a class variable. A class variable is a
variable that’s the same for every instance of the class.

You can define a class variable by including it in the indented part of your class definition, and you can access all of
an object’s class variables with object.variable syntax.
"""
class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)
# prints "Rockstar"
"""
Above we defined the class Musician, then instantiated drummer to be an object of type Musician. We then printed out the
drummer’s .title attribute, which is a class variable that we defined as the string “Rockstar”.

If we defined another musician, like guitarist = Musician() they would have the same .title attribute.
Instructions
1.

You are digitizing grades for Jan van Eyck High School and Conservatory. At Jan van High, as the students call it, 65 is
the minimum passing grade.

Create a Grade class with a class attribute minimum_passing equal to 65.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
