load_file_in_context('script.py')
try:
  check_type('medium_pizza', Circle)
  check_type('teaching_table', Circle)
  check_type('round_room', Circle)
except NameError:
  fail_tests("Is `Circle` a class that is defined?")

if not all(hasattr(medium_pizza, 'radius'), hasattr(teaching_table, 'radius'), hasattr(round_room, 'radius')):
  fail_tests("Do your `Circle` objects have a `radius` attribute?")

if (medium_pizza.radius, teaching_table.radius, round_room.radius) != (12 / 2, 36 / 2, 11460 / 2):
  fail_tests("Is the `radius` of your `Circle` objects half the passed in `diameter`?")
pass_tests()
