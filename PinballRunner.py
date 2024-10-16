import pygame
import Renderer
import GameObject
import Vector3
import random

#initialising pygame and configuring basic stuff so the window will pop up
pygame.init()
#screen = pygame.display.set_mode((600,800))
clock = pygame.time.Clock()
running = True
deltaTime = 0
fPS = 0
renderer = Renderer.Renderer((600,800))
gameObjects = []




#testCode

testObject = GameObject.GameObject("Test Object 1",Vector3.Vector3(2,3,4),Vector3.Vector3(1,1,1),Vector3.Vector3(2,3,4))
gameObjects.append(testObject)

testObject = GameObject.GameObject("Test Object 2",Vector3.Vector3(5,5,0),Vector3.Vector3(5,5,1),Vector3.Vector3(2,3,4))
testObject.addSpriteRenderer('Assets\SamruaiDodge1.png')
gameObjects.append(testObject)

    


#basic game loop, everything must run in this loop
while running:
    
    if(len(gameObjects) < 100):
        testObject = GameObject.GameObject("Test Object 2",Vector3.Vector3(random.randrange(0,600),random.randrange(0,800),0),Vector3.Vector3(5,5,1),Vector3.Vector3(2,3,4))
        testObject.addSpriteRenderer('Assets\SamruaiDodge1.png')
        gameObjects.append(testObject)
    else:
        del gameObjects[0]
        testObject = GameObject.GameObject("Test Object 2",Vector3.Vector3(random.randrange(0,600),random.randrange(0,800),0),Vector3.Vector3(5,5,1),Vector3.Vector3(2,3,4))
        testObject.addSpriteRenderer('Assets\SamruaiDodge1.png')
        gameObjects.append(testObject)






    #Should always be as close to back as possible, renders the current frame. ONLY PUT INFRONT OF EVENTS THAT NEED TO BE AFTER
    renderer.renderFrame(gameObjects)

    #this loop must run at the end of the game loop, it will check if pygame has been quit or not (besides the deltatime)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # tracking fps, must be true end of loop
    clock.tick()
    fPS = clock.get_fps()
    deltaTime = clock.tick(fPS)/1000
    print("FPS:" + str(fPS) + "     Deltatime:" + str(deltaTime))


pygame.quit()