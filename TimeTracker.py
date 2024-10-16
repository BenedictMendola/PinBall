import pygame

class TimeTracker():

    def __init__(self):
        self.time = 0
        self.deltaTime = 0
        self.fPS = 0
        self.clock = pygame.time.Clock()

    def updateTime(self):
        self.clock.tick()
        self.fPS = self.clock.get_fps()
        self.deltaTime = self.clock.tick(self.fPS)/1000

