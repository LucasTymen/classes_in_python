load_file_in_context('script.py')
try:
  if type(Grade) is not type:
    fail_tests("Did you define a `Grade` class?")
  grade = Grade()
except NameError:
  fail_tests("Did you define a `Grade` class?")

if hasattr(grade, 'minimum_passing'):
  if grade.minimum_passing == 65:
    pass
  else:
    fail_tests("Is `minimum_passing` equal to `65`?")
else:
  fail_tests("Does `Grade` have a class attribute `minimum_passing`?")
pass_tests()
