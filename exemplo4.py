#Mu Editor - Pygame Zero mode
#Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html
#Library: https://www.aposteriori.com.sg/pygame-zero-helper/
import pgzrun
from pgzhelper import *
from random import randint

WIDTH = 800
HEIGHT = 600

score = 0
life = 1
game_over = False

alien = Actor("alien_1")
alien.images = ["alien_1", "alien_2"]
alien.fps = 15
alien.pos = (WIDTH/2, HEIGHT-100)

icon = Actor("icon")
icon.pos = randint(10, 100), randint(0, 600)


def draw():
    screen.blit("bg_desert", (0, -200))
    if not game_over:
        alien.draw()
        icon.draw()

        screen.draw.text(
            "Pontos: " + str(score),
            (650, 5),
            color="black"
        )

        screen.draw.text(
            "Vidas: " + str(life),
            (550, 5),
            color="black"
        )
    else:
        screen.fill("black")
        screen.draw.text("GAME OVER \nTotal de pontos: " + str(score),
                         (WIDTH / 3, HEIGHT / 2),
                         color="white",
                         fontsize = 60)

    alien.draw()
    icon.draw()

def update():
    global score, life, game_over

    icon_pos()
    move_alien()

    icon_coletado = icon.colliderect(alien)

    if icon_coletado and not game_over:
        score += 1
        icon.pos = (randint(0, 800), -10)
        sounds.boing.play()

    if life == 0:
        game_over = True

def move_alien():
    if keyboard.left:
        alien.animate()
        alien.x -= 2
        alien.flip_x = True
    elif keyboard.right:
        alien.animate()
        alien.x += 2
        alien.flip_x = False


def icon_pos():
    global life

    icon.y += 3
    if icon.y > HEIGHT and not game_over:
        icon.y = 0
        icon.pos = (randint(0, 800), -10)
        sounds.snap.play()
        life -= 1



music.play("grasslands_theme")
music.set_volume(0.1)
pgzrun.go()
