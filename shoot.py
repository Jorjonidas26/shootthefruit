import pgzrun
import pygame
from random import randint
from pgzero import actor

TIME_INTERVAL = 3.0
REPOSITION_INTERVAL = 0.1
POINTS_TIME_RATE = 0.2
scoreTemplate = "I need a {fruit}, your score is {hits} hits"

# define fruit actors
apple = actor.Actor("apple")
orange = actor.Actor("orange")
pineapple = actor.Actor("pineapple")

actors = [apple, orange, pineapple]
fruits = ["apple", "orange", "pineapple"]
# game trackers
do_onload = True
score = 0
game_over = False
fruit = "apple"
fruit_idx = 0
time_left = TIME_INTERVAL

def place_fruit():
    global fruits, fruit, fruit_idx, time_left, score
    time_left = TIME_INTERVAL - score*POINTS_TIME_RATE
    infoObject = pygame.display.Info()
    for actor in actors:
        actor.x = randint(10, infoObject.current_w - 40)
        actor.y = randint(30, infoObject.current_h - 40)
    
    fruit_idx = randint(0, len(fruits)-1)
    fruit = fruits[fruit_idx]


def draw():
    global score, game_over, do_onload, fruit
    screen.clear()
    if do_onload:
        do_onload = False
        place_fruit()
    if game_over:
        score = 0
    else:
        apple.draw()
        orange.draw()
        pineapple.draw()
    screen.draw.text(scoreTemplate.format(hits=score, fruit=fruit), topleft=(10,10))
    

def on_mouse_down(pos):
    '''sovreescribimos el click del raton'''
    global score, game_over, actors, fruit_idx
    
    fruit = actors[fruit_idx]
    if game_over:
        game_over = False
        draw()
    elif fruit.collidepoint(pos):
        score = score + 1
        place_fruit()
    else:
        game_over = True

def update_positions():
    global time_left
    if time_left > 0:
        time_left = time_left - REPOSITION_INTERVAL
    else:
        place_fruit()
        
clock.schedule_interval(update_positions, REPOSITION_INTERVAL)

pgzrun.go()