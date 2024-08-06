#Mu Editor - Pygame Zero mode
import pgzrun
from pgzhelper import  *
from random import randint

WIDTH = 800
HEIGHT = 600

alien = Actor("alien_1")
alien.pos = (WIDTH/2, HEIGHT-132)
alien.scale = 0.5
alien.images = ["alien_1", "alien_2"]
alien.fps = 15

icon = Actor("icon")
icon.pos = (randint(0, 800), -10)
#icon.scale = 1.5

score = 0
life = 5
game_over = False

def draw():
    screen.blit("bg_desert", (0, -150))

    if not game_over:
        alien.draw()
        icon.draw()

        screen.draw.text(
            "Vidas: " + str(score),
            (650, 5),
            color="white"
        )

        screen.draw.text(
            "Vidas: " + str(life),
            (550, 5),
            color="white"
        )
    else:
        screen.draw.text(
            "GAME OVER \nTotal de pontos: " + str(score),
            midtop=(400, 100),

            color="white"
        )

def update():
    global score, life, game_over

    icon_pos()
    move_alien()

    icon_collide_alien = icon.colliderect(alien)

    if icon_collide_alien and not game_over:
        score += 1
        icon.pos = (randint(0, 800), -10)
        sounds.boing.play()

    if life == 0:
        game_over = True

def icon_pos():
    global life

    icon.y += 3
    if icon.y > HEIGHT and not game_over:
        icon.y = 0
        icon.pos = (randint(0, 800), -10)
        sounds.snap.play()
        life -= 1

def move_alien():
    if keyboard.left:
        alien.animate()
        alien.x -= 2
        alien.flip_x = True
        if keyboard.space:
            alien.x -= 3
    elif keyboard.right:
        alien.animate()
        alien.x += 2
        alien.flip_x = False
        if keyboard.space:
            alien.x += 3

music.play("mushroom_theme")
music.set_volume(0.5)

pgzrun.go()
