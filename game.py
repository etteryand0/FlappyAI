from random import randint
from bird import Bird
# from ai import AI

# Obsticle has four parametrs: 1) dynamic X position of top part 2) static Y length of top part
#                              3) dynamic X position of bottom part 4) static Y position of bottom part
#
# Bird has 2 parametrs: 1) static x position 2) dynamic Y position
#
class Game():
  def __init__(self):
    Bird = Bird() # Bird.position
    self.obsticles = []
    self.generate_obsticles()
    self.draw_world()

  def __str__(self):
    return 'HandlerApp'

  def generate_obsticles(self):
    pass

  def loop(self): # key listener, generate_obsticles(), etc
    pass
