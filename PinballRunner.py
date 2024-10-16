import pygame
import Renderer
import GameObject
import Vector3
import Physics
import TimeTracker

#initialising pygame and configuring basic stuff so the window will pop up
pygame.init()
#screen = pygame.display.set_mode((600,800))
timeTracker = TimeTracker.TimeTracker()
running = True
renderer = Renderer.Renderer((600,800))
gravityScale = 1000

#try to keep every object in order by z hight
gameObjects = []




#testCode


testObject = GameObject.GameObject("Test Object 2",Vector3.Vector3(300,400,0),Vector3.Vector3(3,3,1),Vector3.Vector3(2,3,4))
testObject.addRidgidBody(Vector3.Vector3(0,-600,0),0,10)
testObject.addSpriteRenderer('Assets\RedCircle1.png')
gameObjects.append(testObject)

    


#basic game loop, everything must run in this loop
while running:
    

    #delete once game runs naturaly at reasoanple framerate
    for i in range(500000):
        pass



    Physics.addGravityAll(gameObjects,timeTracker.deltaTime,gravityScale)
    Physics.moveObjects(gameObjects,timeTracker.deltaTime)

    #Should always be as close to back as possible, renders the current frame. ONLY PUT INFRONT OF EVENTS THAT NEED TO BE AFTER
    renderer.renderFrame(gameObjects)

    #this loop must run at the end of the game loop, it will check if pygame has been quit or not (besides the deltatime)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # tracking fps, must be true end of loop
    timeTracker.updateTime()
    print("FPS:" + str(timeTracker.fPS) + "     Deltatime:" + str(timeTracker.deltaTime))


pygame.quit()