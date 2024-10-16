import pygame
import Renderer
import GameObject
import Vector3
import Physics
import TimeTracker
import Prefabs

#initialising pygame and configuring basic stuff so the window will pop up
pygame.init()
#screen = pygame.display.set_mode((600,800))
timeTracker = TimeTracker.TimeTracker()
timeTracker.deltaTime = .001
running = True
renderer = Renderer.Renderer((600,800))
gravityScale = 750
gameTicks = 0
#try to keep every object in order by z hight
gameObjects = []




#testCode




gameObjects.append(Prefabs.makeRedCircle(Vector3.Vector3(200,400,0),Vector3.Vector3(1,1,1),Vector3.Vector3(100,-600,0),0,10))


    
gameObjects.append(Prefabs.makeBlueBox(Vector3.Vector3(80,600,0),Vector3.Vector3(0,0,0)))
gameObjects.append(Prefabs.makeBlueBox(Vector3.Vector3(230,600,0),Vector3.Vector3(0,0,0)))
gameObjects.append(Prefabs.makeBlueBox(Vector3.Vector3(380,600,0),Vector3.Vector3(0,0,0)))
gameObjects.append(Prefabs.makeBlueBox(Vector3.Vector3(530,600,0),Vector3.Vector3(0,0,0)))
gameObjects.append(Prefabs.makeBlueBox(Vector3.Vector3(380,400,0),Vector3.Vector3(0,0,0)))
#basic game loop, everything must run in this loop
while running:
    gameTicks += 1





    Physics.addGravityAll(gameObjects,timeTracker.deltaTime,gravityScale)
    Physics.checkAllCollisons(gameObjects)
    Physics.moveObjects(gameObjects,timeTracker.deltaTime)
    #Should always be as close to back as possible, renders the current frame. ONLY PUT INFRONT OF EVENTS THAT NEED TO BE AFTER
    renderer.renderFrame(gameObjects)

    #this loop must run at the end of the game loop, it will check if pygame has been quit or not (besides the deltatime)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # tracking fps, must be true end of loop
    timeTracker.updateTime()
    #print(gameObjects[0].transform.position.y)


pygame.quit()