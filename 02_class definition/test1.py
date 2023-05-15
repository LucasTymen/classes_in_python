load_file_in_context('script.py')
try:
	check_type('facade_1', Facade)
except NameError:
  fail_tests("Is there a `Facade` class defined?")
pass_tests()
