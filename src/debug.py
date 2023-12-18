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
        text = self.font.render(Input.mouse_pos().__str__(), True, MyColor.white)
        display.blit(text, (20,20))

        text = self.font.render(f"Debug: {Debug.drawRect.__str__()}", True, MyColor.white)
        display.blit(text, (20,40))