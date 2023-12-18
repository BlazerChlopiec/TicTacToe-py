import pygame

class Input:

    _keyboard = None
    _old_keyboard = None

    _mouse = None
    _old_mouse = None

    @staticmethod
    def before_update():
        Input._keyboard = pygame.key.get_pressed()
        Input._mouse = pygame.mouse.get_pressed()
        
        if not Input._old_keyboard: Input._old_keyboard = Input._keyboard
        if not Input._old_mouse: Input._old_mouse = Input._mouse

    @staticmethod
    def after_update():
        Input._old_keyboard = Input._keyboard
        Input._old_mouse = Input._mouse

    @staticmethod
    def mouse_pos() -> tuple:
        return pygame.mouse.get_pos()

    @staticmethod
    def key(key):
        return Input._keyboard[key] == True and not Input._old_keyboard[key]
    
    @staticmethod
    def mouse_down(key):
        return Input._mouse[key] == True and not Input._old_mouse[key]
    
    @staticmethod
    def mouse_up(key):
        return Input._mouse[key] == False and Input._old_mouse[key]
    
    @staticmethod
    def mouse_hold(key):
        return Input._mouse[key] == True