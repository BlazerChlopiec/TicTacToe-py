import pygame
from myColor import MyColor
from debug import Debug
from object import Object
from overrides import override

class Sprite(Object):
    def __init__(self, path: str, pos: tuple, size: tuple, z_order: int = 0):
        self.pos = pos
        self.size = size
        self.image = pygame.transform.scale(pygame.image.load(path), size).convert_alpha()
        self.rect = pygame.Rect(pos, size)
        self.z_order = z_order

    @override
    def update(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    @override
    def draw(self, display, color = MyColor.clear):
        if color is not MyColor.clear: self.image.fill(color)

        display.blit(self.image,self.pos)
        
        if Debug.drawRect: 
            pygame.draw.rect(display, MyColor.white, self.rect, width=2)