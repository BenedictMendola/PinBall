import pygame

class Renderer:

    def __init__(self,screenSize: tuple):
        self.screenSize = screenSize
        self.screen = pygame.display.set_mode(screenSize)
        self.backgroundColor = pygame.Color(0,255,0)
    
    def renderFrame(self,objects: list):
       self.screen.fill(self.backgroundColor)
       pygame.display.flip()