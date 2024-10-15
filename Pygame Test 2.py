import pygame
import random
import GameObject



pygame.init()
screen = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()
running = True
deltaTime = 0
backgroundColor = pygame.Color(0,255,0)


# methods

# called at end of every frame, renders every object and background
def renderFrame(backgroundColor, gameObjects):
    screen.fill(backgroundColor)
    pygame.display.flip()


#Creating essentail vars

gameObjects = []

#main loop
while running:

    

    



    #check if user quits game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    renderFrame(backgroundColor,gameObjects)


    