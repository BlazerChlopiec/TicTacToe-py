import pygame
import os
from sprite import Sprite
from myColor import MyColor
from debug import Debug
from button import Button
from input import Input
from itertools import combinations

pygame.init()
pygame.mouse.set_visible(0)

res = (800, 450)
display = pygame.display.set_mode((res[0], res[1]))
pygame.display.set_caption("jaja")

font = pygame.font.Font(None, 25)
button_font = pygame.font.Font(None, 75)
clock = pygame.time.Clock()

spr = "Sprites" # define the sprite folder

objects = []

def sort_objects():
    global objects
    objects = sorted(objects, key=lambda obj: obj.z_order if hasattr(obj, "z_order") else 0)

header_text = ""
def header_show_turn():
    global header_text
    header_text = "Place a Circle" if cross_turn == False else "Place a Cross"

win_state = False
cross_turn = False
cross_tiles = []
circle_tiles = []


# OBJECTS
cursor = Sprite(os.path.join(spr, "cursor.png"), (0,0), (50, 50), z_order=10)
objects.append(cursor)

def tictactoe_button(tile, win_karma):
    spacing = (110, 110)
    sprite_size = (100, 100)
    button = Button(button_font, "", os.path.join(spr, "button.png"), (res[0]/2 - sprite_size[0]/2 + (spacing[0] * tile[0]),
                                                                       res[1]/2 - sprite_size[1]/2 + (spacing[1] * tile[1])), sprite_size)
    button.win_karma = win_karma

    def check_win():
        global cross_tiles
        global circle_tiles
        global win_state
        global header_text
        
        # this win check uses the win_karma solution
        # basically every tile has a value
        # we loop through every combination of 3 of a set of tiles (circle, cross)
        # if the value is equal to 15 the iterated set has won

        for combo in combinations(circle_tiles, 3):
            circle_karma = 0

            for circle in combo:
                circle_karma += circle.win_karma

            if circle_karma == 15: 
                win_state = True
                header_text = "Circle WON" 

        for combo in combinations(cross_tiles, 3):
            cross_karma = 0

            for cross in combo:
                cross_karma += cross.win_karma

            if cross_karma == 15: 
                win_state = True
                header_text = "Cross WON"

    def click(b):
        global cross_turn

        if hasattr(b, "has_been_pressed") and b.has_been_pressed == True or win_state == True: return
        b.has_been_pressed = True

        if cross_turn:
            b.text = "X"
            b.text_color = MyColor.red
            cross_tiles.append(b)
        else:
            b.text = "O"
            b.text_color = MyColor.green
            circle_tiles.append(b)
        cross_turn = not cross_turn

        check_win()

        if not win_state: header_show_turn()

    button.on_click = click
    objects.append(button)

#top
tictactoe_button((-1, -1), 4)
tictactoe_button((0, -1), 9)
tictactoe_button((1, -1), 2)

#middle
tictactoe_button((-1, 0), 3)
tictactoe_button((0, 0), 5)
tictactoe_button((1, 0), 7)

#bottom
tictactoe_button((-1, 1), 8)
tictactoe_button((0, 1), 1)
tictactoe_button((1, 1), 6)


def reset_click(b):
    global win_state 
    global cross_turn
    global header_text

    win_state = False
    cross_turn = False
    header_show_turn()

    for c in circle_tiles:
        if hasattr(c, "has_been_pressed"): c.has_been_pressed = False
        c.text = ""

    for c in cross_tiles:
        if hasattr(c, "has_been_pressed"): c.has_been_pressed = False
        c.text = ""

    circle_tiles.clear()
    cross_tiles.clear()

reset_size = (180,40)
reset_button = Button(font, "Reset", os.path.join(spr, "button.png"), (res[0]/2 - reset_size[0]/2, res[1]-35 - reset_size[1]/2), reset_size)
reset_button.on_click = reset_click
objects.append(reset_button)

debug = Debug(font)
objects.append(debug)
#

header_show_turn()
sort_objects()

running = True
while running:

    Input.before_update()
    
    for e in pygame.event.get():
        if (e.type == pygame.QUIT): running = False

    if Input.key(pygame.K_ESCAPE): running = False

    display.fill((20, 20, 20))

    cursor.pos = Input.mouse_pos()

    # header
    header_col = MyColor.red if not cross_turn else MyColor.green
    header_rendered = font.render(header_text, True, MyColor.white if not win_state else header_col)
    header_rect = header_rendered.get_rect(center=(res[0]/2, 30))
    display.blit(header_rendered, header_rect)
    #
    
    for s in objects:
        s.update()
    
    for s in objects:
        s.draw(display)

    Input.after_update()

    pygame.display.update()