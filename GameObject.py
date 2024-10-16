import Vector3
import Transform
import SpriteRenderer
import Physics


#All things are gameobjects, and their components. 
# a game object at minnimum has a transform, but other components can be added
class GameObject:

    def __init__(self,name: str,position: Vector3.Vector3,scale: Vector3.Vector3,vectorAngle:Vector3.Vector3):
        self.name = name
        self.transform = Transform.Transform(position,scale,vectorAngle)
        self.spriteRender = None
        self.ridgidbody = None

    def addSpriteRenderer(self,imagePath: str):
        self.spriteRender = SpriteRenderer.SpriteRenderer(imagePath)

    def addRidgidBody(self,velocity:float,angularV: float,mass: float):
        self.ridgidbody = Physics.RigidBody(velocity,angularV,mass)
        
        


