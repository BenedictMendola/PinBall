import Vector3


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