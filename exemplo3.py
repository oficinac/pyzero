#Mu Editor - Pygame Zero mode
# Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

alien = Actor("alien")
alien.pos = (WIDTH / 2, HEIGHT / 2)

bee = Actor("bee")
bee.pos = randint(800, 1600), randint(10, 100)

up = False
game_over = False
vidas = 2
score = 0

def draw():
    if not game_over:
        screen.blit("grass", (0, 0))
        screen.draw.text("Pontos: " + str(score), (700, 5), color="black")

        screen.draw.text("Vidas: " + str(vidas), (600, 5), color="black")

        alien.draw()
        bee.draw()

    else:
        screen.fill("black")
        screen.draw.text("GAME OVER \nFinal pontos: " + str(score),
                         (WIDTH / 2, HEIGHT / 2),
                         color="black")

def update():
    global life, game_over

    alien_pos()
    bee_pos()

    if vidas == 0:
        game_over = True

def on_mouse_down():
    global up
    up = True
    alien.y -= 50
    alien.image = "alien_hurt"

def on_mouse_up():
    global up
    up = False
    alien.image = "alien"

def bee_pos():
    global score
    if bee.x > 0:
        bee.x -= 10
    else:
        bee.pos = randint(800, 1600), randint(10, 100)
        if not game_over:
            score += 1


def alien_pos():
    #gravity
    if not up:
        alien.y += 1

    if alien.top < 0 or alien.bottom > 580:
        alien.y = HEIGHT / 2

def alien_pos_after_collide():
    alien.x = WIDTH / 4
    alien.y = HEIGHT / 2



pgzrun.go()