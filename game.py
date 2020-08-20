# Obsticle has four parametrs: 1) dynamic X position of itself 2) static Y length of top part
#                              3) static top Y position of bottom part
#
# Bird has 2 parametrs: 1) static x position 2) dynamic Y position
# Generation ends if all birds hit obcticles 

class Game():
  def __init__(self):
    from bird import Bird
    from random import randint
    import time
    import os
    
    self.time = time # controle fps
    self.Bird = Bird() # Bird.position
    self.clear = lambda: os.system('clear')
    self.randint = randint

    self.obsticles = []

    self.worldSize = [30,10] # [x,y]
    self.world = []
    self.generate_obsticles()
    
    self.alive = True # to loop process

  def __str__(self):
    return 'HandlerApp'
 
  def game_over(self):
    import sys
    self.clear()
    self.draw_world()
    sys.exit('\nYou died')

  def generate_obsticles(self):
    if len(self.obsticles) <= 7 and len(self.obsticles) != 0:
      distance = self.worldSize[0] - self.obsticles[-1][0] # distance from end to last obsticle
      if distance > 5: # [x,topY,bottomY]
        if distance >= 6: # if passed too much (distance is large) create obsticle
          pass
        else:
          if self.randint(1,3) % 2 != 0: # randomly choose if we should create obsticle
            return False # pass. Dont create obsticle
        max_topY = 5
        min_bottomY = 3
        while True:
          topY = self.randint(0,max_topY)
          if topY < self.obsticles[-1][1]: # if topY is higher than last obsticle`s topY
            # (self.Bird.position[1] (Y) + distance) > topY
            if (self.Bird.position[1] + distance) > topY: # Bird can survive, able to fit hole
              bottomY = self.randint(topY+1+min_bottomY,self.worldSize[1]) # +1 because topY cant be hole. +3 becaue 3 is minimum of hole
              self.obsticles.append([self.worldSize[0]-1,topY,bottomY])
              break # stop the loop
            else: # Bird cant fit hole
              max_topY = topY-1 # topY is not valid. Resize max_topY
              # loop restarts

          elif topY > self.obsticles[-1][1]: # if last obsticle`s topY is higher than topY
            # is bird able to fit hole? Ie survive
            hole = range(topY+1,topY+1+min_bottomY) # size of potentional hole. +1 because topY cant be hole
            able_to_jump = filter(lambda n: (self.Bird.position[1]-n) % 2 == 0, hole) # filter even numbers if -n
            jump_quote = [i for i in list(able_to_jump) if (self.Bird.position[1]-i)/2 <= distance] # is bird able to jump thru without hitting a wall? Lets learn it
            if len(jump_quote) > 0: # checking if bird can survive
              # yes. Bird can survive
              self.obsticles.append([self.worldSize[0]-1,topY,topY+min_bottomY])
              break # stop the loop
            else: # bird will hit wall
              min_bottomY += 1 # min_bottomY is not enough. Expand it
              # loop restarts
          else: # else topY is equivalent of last obsticle`s topY
            pass # just restart loop. Lets ignore this script. Maybe next time I`ll add it
            # loop restarts 
      
      else: # distance is too small. abort
        return False
        
    elif len(self.obsticles) == 0:
      topY = self.randint(0,3)
      bottomY = topY+4
      self.obsticles.append([self.worldSize[0]-1,topY,bottomY])
    else:
      return False

    return True # obsticle added

  def handle_obsticles(self):
    self.Bird.position[1] += 1 # fall `cause gravity
    for obsticle in self.obsticles:
      obsticle[0] -= 1
    if self.obsticles[0][0] < 0:
      self.obsticles.pop(0)

    if self.Bird.position[1] == self.worldSize[1]-2: # check for game_over. -1 because list starts with [0]
      self.alive = False
    else:
      for obsticle in self.obsticles:
        if self.Bird.position[0] == obsticle[0]:
          if self.Bird.position[1] <= obsticle[1] or self.Bird.position[1] >= obsticle[2]:
            self.alive = False

  def draw_world(self):
    self.world = [' '*self.worldSize[0] for i in range(0,self.worldSize[1])]
    
    id_ = 0
    for frame in self.world:
      frame = frame[1:].split(' ') # len(frame) = 80 # >>> ['','','','',...,'','']
      if self.Bird.position[1] == id_:
        frame[self.Bird.position[0]] = '@'
      for obsticle in self.obsticles: # one-by-one draw obsticles
        if id_ <= obsticle[1] or id_ >= obsticle[2]: # if frame has obsticle
          frame[obsticle[0]] = '|'
      
      item_id = 0
      for item in frame: # replace all '' with space ' '
        if item == '' and id_ != 9:
          frame[item_id] = ' '
        elif id_ == 9:
          frame[item_id] = '#'
        item_id += 1
      
      output = ''
      for string in frame:
        output += string
      self.world[id_] = output
      id_ += 1
      # loop restarts

    self.clear()
    [print(i) for i in self.world]
    self.world_backup = self.world
    print(self.obsticles)

  def loop(self): # key listener, generate_obsticles(), etc
    while self.alive:
      self.generate_obsticles()
      self.draw_world()
      self.time.sleep(0.5)
      self.handle_obsticles()

    self.game_over()

    # while self.alive:
    #   self.draw_world()
    #   self.time.sleep(0.5)

    #   self.handle_obsticles()
    #   self.generate_obsticles()
      
# Debug
import multiprocessing

def listen(Game):
  import keyboard
  while True:
    try:
      if keyboard.is_pressed('q'):
        print('Truesldfk')
        Game.Bird.jump()
    except:
      import sys
      sys.exit()

Game = Game()
game_loop = multiprocessing.Process(target=Game.loop)
key_loop = multiprocessing.Process(target=listen,args=(Game,))
game_loop.start()
key_loop.start()
key_loop.join()
game_loop.join()
