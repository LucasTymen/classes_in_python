load_file_in_context('script.py')
try:
  Circle
except NameError:
  fail_tests("Is there a class defined called `Circle`?")
try:
  circle1 = Circle(1)
  circle2 = Circle(4)
  circle3 = Circle(10)
except TypeError:
  fail_tests("Does `Circle` have a constructor that takes two parameters: `self` and `diameter`?")

if str(circle1) != "Circle with radius 1":
  fail_tests("Does `Circle` have a `__repr__` method that returns 'Circle with radius <X>' where <X> is the radius?")
