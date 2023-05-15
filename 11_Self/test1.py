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

if not hasattr(circle1, 'radius'):
  fail_tests("Does `Circle`'s constructor define `self.radius`?")
if (circle1.radius, circle2.radius, circle3.radius) != (1 / 2, 4 / 2, 10 / 2):
  fail_tests("Is `self.radius` set to half the diameter?")
pass_tests()
