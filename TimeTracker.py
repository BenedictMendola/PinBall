import pygame
import time

class TimeTracker():

    # def __init__(self):
    #     self.time = 0
    #     self.deltaTime = 0
    #     self.fPS = 0
    #     self.clock = pygame.time.Clock()

    # def updateTime(self):
    #     self.clock.tick()
    #     self.fPS = self.clock.get_fps()
    #     self.deltaTime = self.clock.tick(self.fPS)/1000
    #     self.deltaTime = 0.001


    def __init__(self):
        self.time = 1
        self.deltaTime = .01
        self.lastTime = .999999

    def updateTime(self):
        self.deltaTime = time.time() - self.lastTime
        self.lastTime = time.time()
        if (self.deltaTime > 2):
            self.deltaTime = .01
