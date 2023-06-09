class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
print(medium_pizza.circumference())

teaching_table = Circle(36)
print(teaching_table.circumference())

round_room = Circle(11460)
print(round_room.circumference())
