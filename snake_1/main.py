import pygame
from pygame.constants import KEYDOWN
import helper_functions

# init pygame
pygame.init()

# create font
system_fonts = pygame.font.get_fonts()
print(system_fonts)

my_font = pygame.font.SysFont(system_fonts[0], size = 48, bold = True, italic = False)
score = 0

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

# snake current position
cur_pos = [300,200]
direction = "down"
snake_body = [
   [300,200],
   [300,180],
   [300,160],
   [300,140]
]

"""game loop"""
running = True
while running:
   """ Handle events """
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == KEYDOWN:
         if event.key == pygame.K_ESCAPE: # escape key
            running = False
         if event.key == pygame.K_w and direction != "down": # up direction
            direction = "up"
            # cur_pos[1] -= 20
         if event.key == pygame.K_s and direction != "up": # down direction
            direction = "down"
            # cur_pos[1] += 20
         if event.key == pygame.K_a and direction != "right": # left direction
            direction = "left"
            # cur_pos[0] -= 20
         if event.key == pygame.K_d and direction != "left": # right direction
            direction = "right"
            # cur_pos[0] += 20

   
   """ update our game state """
   if direction == "up":
      cur_pos[1] -= 20
   if direction == "down":
      cur_pos[1] += 20
   if direction == "left":
      cur_pos[0] -= 20
   if direction == "right":
      cur_pos[0] += 20
   
   if cur_pos[0] < 0:
      cur_pos[0] = 0
      running=False
   if cur_pos[0] > width-20:
      cur_pos[0] = width-20
      running=False

   if cur_pos[1] < 0:
      cur_pos[1] = 0
      running=False
   if cur_pos[1] > height-20:
      cur_pos[1] = height-20
      running=False


   # snake movement
   snake_body.insert(0, list(cur_pos))
   snake_body.pop()

   # handle loose state
   
   
   """ draw to our screen """
   # clear screen
   screen.fill("white")

   # draw text to screen
   helper_functions.draw_text(f'Score: {score}', (20,20), "red", my_font, screen)
   helper_functions.draw_text(f'Snake!', (300,20), "blue", my_font, screen)

   # draw snake
   for body in snake_body:
      pygame.draw.rect(
         surface = screen,
         color = "green",
         rect=pygame.Rect(body[0], body[1], 20, 20)
          )

   # draw rectangle
   """
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
"""
   # update screen
   pygame.display.flip()

   #fps
   dt = clock.tick(speed) / 1000

# quit pygame
pygame.quit()
