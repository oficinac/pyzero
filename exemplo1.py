#Mu Editor - Pygame Zero mode
# Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html
import pgzrun

alien = Actor('alien')
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.eep.play()
        alien.image = 'alien_hurt'
    else:
        alien.image = 'alien'

pgzrun.go()