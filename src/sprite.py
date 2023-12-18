import pygame
from myColor import MyColor
from debug import Debug
from object import Object
from overrides import override

class Sprite(Object):
    def __init__(self, path: str, pos: tuple, size: tuple, z_order: int = 0):
        self.pos = pos
        self.size = size
        self.image = pygame.transform.scale(pygame.image.load(path), size)
        self.rect = pygame.Rect(pos, size)
        self.z_order = z_order

    @override
    def update(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    @override
    def draw(self, display, color = MyColor.clear):
        if color is not MyColor.clear: self.change_color(self.image, color)
        display.blit(self.image, self.pos)

        
        if Debug.drawRect: 
            pygame.draw.rect(display, MyColor.white, self.rect, width=2)

    def change_color(self, image, color) -> pygame.Surface:
        colored = pygame.Surface(image.get_size())
        colored.fill(color)
    
        self.image = image.convert_alpha()
        self.image.blit(colored, (0, 0), special_flags = pygame.BLEND_PREMULTIPLIED)