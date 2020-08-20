class Bird():
  def __init__(self):
    self.position = [2,2] # [x,y]

  def __str__(self):
    return "BirdApp"

  def jump(self):
    self.position[1] -= 2
    return True
