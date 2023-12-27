import pygame
from myColor import MyColor
from object import Object
from overrides import override
from input import Input

class Debug(Object):
    drawRect = False

    def __init__(self, font):
        self.font = font

    @override
    def update(self):
        if Input.key(pygame.K_TAB): Debug.drawRect = not Debug.drawRect
        
    @override
    def draw(self, display, color = MyColor.clear):
        display.blit(self.font.render(Input.mouse_pos().__str__(), True, MyColor.white), (20,20))
        display.blit(self.font.render(f"Debug: {Debug.drawRect.__str__()}", True, MyColor.white), (20,40))
        display.blit(self.font.render("Use TAB", True, MyColor.white), (20, 60))
