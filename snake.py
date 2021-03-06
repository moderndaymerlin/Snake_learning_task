# -*- coding: utf-8 -*-

#snake game

"""
Created on Tue Dec 19 20:50:23 2017

@author: John
"""

import pygame #module which introduces graphics, sounds, vector handling, inputs (interrupts)
import sys #system - exit functions, fundamentals
import random #calculate random number as co-ordinates
import time #allows for a delay to be introduced after 'death'

error_ch = pygame.init() #initialises the pygame module to check for errors. try print(pygame.init()) which prints out the number of successful processes and failures

if error_ch[1]>0:
    print("Error loading pygame module, had {0} errors".format(error_ch[1]))
    sys.exit(-1) #sys exits with the exit command -1
else:
    print("pygame successfully loaded")

#create the playable surface
surface = pygame.display.set_mode((720, 460)) #creates the playable surface and defines the size
pygame.display.set_caption("DDA Snake Challenge")

#choose colours to use
red = pygame.Color(240,0,0) #formatted as (r,g,b)
blue = pygame.Color(0,0,240)
green = pygame.Color(0,240,0)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
yellow = pygame.Color(180,180,0)

#FPS controller - 
fpscontroller = pygame.time.Clock()

#initialise game elements position
snakepos = [100,50] #[x,y] starting position of the snake's head
snakebody = [[100,50],[90,50],[80,50]] #[x,y] starting position of the 3 initial elements of the snake body

foodpos = [random.randrange(1,72)*10,random.randrange(1,46)*10] #we want a multiple of 10 since that's the size of the snake head
foodspawn = True

direction = 'RIGHT' #the direction in which the snake moves at the start of the game
changeto = direction 

score = 0

#game over function
def gameover():
    myfont = pygame.font.SysFont('monaco', 120)
    gameosur = myfont.render('Game over', True, red)
    gorect = gameosur.get_rect()
    gorect.midtop = (360,15)
    surface.blit(gameosur,gorect)
    showscore(2)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

def showscore(choice=1):
    sfont = pygame.font.SysFont('monaco', 24)
    scoresur = sfont.render('Score: {0}'.format(score),True,black)
    srect = scoresur.get_rect()
    if choice == 1:
        srect.midtop = (80,10)
    else:
        srect.midtop = (360,120)
    surface.blit(scoresur,srect)

#main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    #validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakepos[0] += 10
    if direction == 'LEFT':
        snakepos[0] -= 10
    if direction == 'UP':
        snakepos[1] -= 10
    if direction == 'DOWN':
        snakepos[1] += 10

    #body mechanics
    snakebody.insert(0,list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        score += 1
        foodspawn = False
    else:
        snakebody.pop()
        
    if foodspawn == False:
        foodpos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodspawn = True
    
    surface.fill(white)
    
    for pos in snakebody:
        pygame.draw.rect(surface,green,pygame.Rect(pos[0],pos[1],10,10))
    
    pygame.draw.rect(surface,yellow,pygame.Rect(foodpos[0],foodpos[1],10,10))
    
    if snakepos[0] > 710 or snakepos[0] < 0:
        gameover()
    if snakepos[1] > 450 or snakepos[1] < 0:
        gameover()
    
    for block in snakebody[1:]:
        if snakepos[0] == block[0] and snakepos[1] == block[1]:
            gameover()
    
    showscore()
    pygame.display.flip()
    fpscontroller.tick(23)










