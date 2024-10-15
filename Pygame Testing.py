# Example file showing a circle moving on screen
import pygame



#setup pygame to boot up the window
pygame.init()
screen = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()
running = True
deltaTime = 0
global backgroundColor
backgroundColor = pygame.Color(0,255,0)


    
r = 0
a = True
#game loop
while running:
    
    #check if user quits game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    backgroundColor = pygame.Color(255 - r % 255,r % 255,r % 255)

    if(a):
        r+= 1
    else:
        r -= 1
    if (r == 254):
        a = False
    if (r == 0):
        a = True
    screen.fill(backgroundColor)
    pygame.display.flip()
    pygame.time.wait(5)



pygame.quit()