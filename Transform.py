import Vector3

class Transform():

    def __init__(self,position: Vector3.Vector3,scale: Vector3.Vector3,vectorAngle: Vector3.Vector3):

        #should allways be a vector3
        self.position = position
        self.scale = scale
        self.vectorAngle = vectorAngle
