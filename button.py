import pygame
from sprite import Sprite
from myColor import MyColor
from overrides import override
from pygame import Color
from input import Input

class Button(Sprite):
    def __init__(self, font, text: str, path: str, pos: tuple, size: tuple, z_order: int = 0):
        super().__init__(path, pos, size, z_order)
        self.font = font
        self.text = text
        self.text_color = MyColor.white

        self.on_click = None
        self.on_hold = None

        self.holding = False

    @override
    def update(self):
        super().update()

        self.hovering = self.rect.collidepoint(Input.mouse_pos())
        if self.hovering and Input.mouse_down(0): 
            self.holding = True
            if self.on_click: self.on_click(self)
    
        elif self.holding and self.on_hold: self.on_hold(self)

        if Input.mouse_up(0): self.holding = False

    @override
    def draw(self, display, color = MyColor.clear):
        super().draw(display, Color(80,80,80) if self.hovering else Color(40,40,40))

        rendered_text = self.font.render(self.text, True, self.text_color)
        text_rect = rendered_text.get_rect(center = (self.pos[0] + self.rect.width/2, self.pos[1] + self.rect.height/2))
        
        display.blit(rendered_text, text_rect)