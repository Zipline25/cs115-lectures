import pygame
age = 30
age2 = 15

if age > 21:
  print ('you are an adult')
  print ('you are old')
else:
  print('you are young')


difference = age - age2
if difference >= 0:
  print("positive or zero")
elif difference > 5:
  print("big number")
elif difference < 0:
  print('negative')

if difference > 5:
  print('big number')


counter = 0
while counter <= 10:
  print(counter)
  counter += 1

inventory = ['sword','shield','key']
for item in inventory:
  print(item)

is_game_paused = True
is_dead = True
if is_game_paused or is_dead:
  print('game paused')
else:
  print('game not paused')

if is_game_paused and is_dead:
  print('game over')

health = 50
if health <= 0:
  is_dead = True