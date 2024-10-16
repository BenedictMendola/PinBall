import Vector3
import Transform


#All things are gameobjects, and their components. 
# a game object at minnimum has a transform, but other components can be added
class GameObject:

    def __init__(self,name: str,position: Vector3.Vector3,scale: Vector3.Vector3,vectorAngle:Vector3.Vector3):
        self.name = name
        self.transform = Transform.Transform(position,scale,vectorAngle)
        self.spriteRender = None

        
        


