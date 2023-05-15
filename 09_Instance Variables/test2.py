load_file_in_context('script.py')
check_type('alternative_rocks', Store)
check_type('isabelles_ices', Store)
if not hasattr(alternative_rocks, 'store_name') or not hasattr(isabelles_ices, 'store_name'):
  fail_tests("Do both `alternative_rocks` and `isabelles_ices` have `store_name` attributes?")
if alternative_rocks.store_name != "Alternative Rocks":
  fail_tests("Is `alternative_rocks`'s `store_name` set to 'Alternative Rocks'?")
if isabelles_ices.store_name != "Isabelle's Ices":
  fail_tests("Is `isabelles_ices`'s `store_name` set to 'Isabelle's Ices'?")
pass_tests()
