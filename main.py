import pygame
import os
from sprite import Sprite
from myColor import MyColor
from debug import Debug
from button import Button
from input import Input

pygame.init()
pygame.mouse.set_visible(0)

display = pygame.display.set_mode((1600/2, 900/2))
pygame.display.set_caption("jaja")

font = pygame.font.Font(None, 25)
clock = pygame.time.Clock()

spr = "Sprites" # define the sprite folder

objects = []

def sort_objects():
    global objects
    objects = sorted(objects, key=lambda obj: obj.z_order if hasattr(obj, "z_order") else 0)

# OBJECTS
cursor = Sprite(os.path.join(spr, "cursor.png"), (0,0), (50, 50), z_order=10)
objects.append(cursor)

button = Button(font, "Whatever", os.path.join(spr, "button.png"), (100,100), (100, 100))
def button_hold(s):
    m = Input.mouse_pos()
    s.pos = (m[0] - s.size[0]/2, m[1] - s.size[1]/2)
button.on_hold = button_hold
objects.append(button)

debug = Debug(font)
objects.append(debug)
#

sort_objects()

running = True
while running:
    Input.before_update()
    
    for e in pygame.event.get():
        if (e.type == pygame.QUIT): running = False

    if Input.key(pygame.K_ESCAPE): running = False

    display.fill((20, 20, 20))

    cursor.pos = Input.mouse_pos()

    for s in objects:
        s.update()
    
    for s in objects:
        s.draw(display)
    
    Input.after_update()

    pygame.display.update()