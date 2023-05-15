load_file_in_context('script.py')
try:
	full_equality('facade_1_type', Facade)
except NameError:
  fail_tests("Is there a `Facade` class defined?")
pass_tests()
