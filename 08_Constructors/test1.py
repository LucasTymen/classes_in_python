load_file_in_context('script.py')
try:
  Circle
except NameError:
  fail_tests("Is there a class defined called `Circle`?")
try:
  circle = Circle(1)
except TypeError:
  fail_tests("Does `Circle` have a constructor that takes two parameters: `self` and `diameter`?")
pass_tests()
