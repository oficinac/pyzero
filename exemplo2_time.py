#Mu Editor - Pygame Zero mode
# Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html
import pgzrun
from random import randint # biblioteca MATH - random
import time

score = 0
game_over = False


WIDTH = 400
HEIGHT = 400

alien = Actor("alien")
alien.pos = 200,200 # WIDTH / 2   HEIGHT / 2

icon = Actor("icon")
icon.pos = randint(20,380),randint(20,380)#sorteio

def draw():
    screen.fill("green")
    screen.draw.text("Pontos " + str(score), color="black", bottomleft=(10,400), fontsize=50)
    alien.draw()
    icon.draw()

    if game_over:
        screen.fill("black")
        screen.draw.text("Pontos " + str(score), color="white", topleft=(100,200), fontsize=60)


def update():

    global score

    #print(alien.x)
    #print(alien.y)
    if keyboard.left:
        alien.x = alien.x - 2 #alien.x -= 2
    elif keyboard.right:
        alien.x = alien.x + 2 #alien.x += 2
    elif keyboard.up:
        alien.y = alien.y - 2
    elif keyboard.down:
        alien.y = alien.y + 2

    #colisão
    icon_coletado = alien.colliderect(icon) #True
    #print(icon_coletado)
    if icon_coletado:# == True
        score = score + 10
        icon_pos()

def icon_pos():
    icon.pos = randint(20,380), randint(20,380)
    print(icon.x, icon.y)

def tempo():
    global game_over
    game_over = True

clock.schedule(tempo, 15)#tempo em segundos
pgzrun.go()