import pygame
from time import sleep
from random import randint

apple = Actor("apple")
scoreTemplate = "your score is {hits} hits"
points = 0

def draw():
    screen.clear()
    apple.draw()
    
def place_apple():
    infoObject = pygame.display.Info()
    apple.x = randint(10, infoObject.current_w - 40)
    apple.y = randint(10, infoObject.current_h - 40)

def on_mouse_down(pos):
    '''sovreescribimos el click del raton'''
    global points
    if apple.collidepoint(pos):
        print("good shot!")
        points = points + 1
        print(scoreTemplate.format(hits=points))
        place_apple()
    else:
        print("You missed!")
        sleep(5)
        quit()

place_apple()
