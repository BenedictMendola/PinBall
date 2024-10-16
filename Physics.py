import Vector3
import VectorMath


class RigidBody:
    
    def __init__(self,velocity:Vector3.Vector3,angularVelocity:float,mass:float):
        self.velocity = velocity
        self.angularVelocity = angularVelocity
        self.mass = mass



    #F = M*a
    def addForce(self,force:Vector3.Vector3): # this excludes gravity
        self.velocity.x +=  (self.mass/force.x)
        self.velocity.x += (self.mass/force.x)
        self.velocity.z += (self.mass/force.z)
    def addGravity(self,gravity: float,deltaTime: float):
        self.velocity.y += deltaTime * gravity
        #print("addedGrav: "+ str(deltaTime * gravity))


def moveObjects(gameObjects,deltaTime):
    for object in gameObjects:
        if (object.ridgidbody != None):
            object.transform.position.x += object.ridgidbody.velocity.x * deltaTime
            object.transform.position.y += object.ridgidbody.velocity.y * deltaTime
            object.transform.position.z += object.ridgidbody.velocity.z * deltaTime
def addGravityAll(gameObjects,deltaTime,gravityScale):
    for object in gameObjects:
        if (object.ridgidbody != None):
                object.ridgidbody.addGravity(gravityScale,deltaTime)

#all of the edges have a slope, if at least two of the sides slopes are past it but not the ones on the opposite side.

class Collider: #normaly a box collider
    def __init__(self,xMax: float,xMin:float,yMax:float,yMin:float):
        self.xMax = xMax
        self.xMin = xMin
        self.yMax = yMax
        self.yMin = yMin

def checkIfColliding(object1,object2):

    

    col1 = object1.collider
    col2 = object2.collider

    x1 = object1.transform.position.x
    x2 = object2.transform.position.x
    y1 = object1.transform.position.y
    y2 = object2.transform.position.y

    #print(f"Object 1:{x1,y1}    object 2 {x2,y2}")

    oneYOver = ((y1 - col1.yMax < y2 + col2.yMin) and (y1 + col1.yMin > y2 - col2.yMin))
    oneXOver = (x1 - col1.xMax < x2 + col2.xMax) and (x1 - col1.xMax > x2 - col2.xMax)

    #makes sure that one but not both of the vertical sides of col 1 is greater than col 2
    #oneXOver = ((col1.xMax + x1 > col2.xMax + x2) and (col1.xMin + x1 < col2.xMax + x2) or (col1.xMin + x1 < col2.xMin + x2) and (col1.xMax + x1 > col2.xMin + x2))
    #oneYOver = ((col1.yMax + y1 > col2.yMax + y2) and (col1.yMin + y1< col2.yMax + y2) or (col1.yMin +y1 < col2.yMin+ y2) and (col1.yMax +y1> col2.yMin+y2))

    if(oneXOver and oneYOver): 
        return True
    return False


def collison(gameObjects: list, o1 : int, o2: int):
    #Apply forces to ones with rigid bodys
    object1 = gameObjects[o1]
    object2 = gameObjects[o2]

    
    if(object1.ridgidbody != None):
        #determining which dir to canncel
        if (object2.transform.position.y - object2.collider.yMax > object1.transform.position.y > object2.transform.position.y - object2.collider.yMax):
            object1.ridgidbody.velocity.x = -object1.ridgidbody.velocity.x
        else:
            object1.ridgidbody.velocity.y = -object1.ridgidbody.velocity.y

        
        #object1.ridgidbody.velocity = VectorMath.mul(object1.ridgidbody.velocity,Vector3.Vector3(-1,-1,-1))
        

def checkAllCollisons(gameObjects):

    #this method only needs to check all active rigid body objects to see if their colliding.
    i = 0
    while(i < len(gameObjects)):
        if(gameObjects[i].ridgidbody != None):
            j = 0
            while(j < len(gameObjects)):
                if((i != j and gameObjects[j].collider != None)and checkIfColliding(gameObjects[i],gameObjects[j])):
                    collison(gameObjects,i,j)
                j+=1

        i+=1










