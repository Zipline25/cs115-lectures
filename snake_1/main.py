import pygame

# init pygame
pygame.init()

# window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# set window title
pygame.display.set_caption("snake")

# fps
clock = pygame.time.Clock()
dt = 0
speed = 10
"""game loop"""
running = True
while running:
  """ Handle events """
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  """ update our game state """
  """ draw to our screen """
  # clear screen
  screen.fill("white")

  # draw rectangle
  pygame.draw.rect(screen, 
                   (0,255,0), 
                   pygame.Rect((100,200),(100,50))
                  )

  pygame.draw.circle(screen, 
                     "blue", 
                     (100,200), 40
                    )

  pygame.draw.line(screen, 
                   "red", 
                   (100,100), (200,200), 5
                  )

  pygame.draw.ellipse(surface=screen, 
                      color="red", 
                      rect=pygame.Rect((100,100), (100,500))
                     )

  # update screen
  pygame.display.flip()

  #fps
  dt = clock.tick(speed) / 1000

# quit pygame
pygame.quit()
