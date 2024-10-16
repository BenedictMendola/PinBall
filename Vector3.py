import math

class Vector3:

    def __init__(self, xPos:float, yPos:float, zPos:float):
        self.x = xPos
        self.y = yPos
        self.z = zPos
    
    def getMagnitude(self):
        return round(math.sqrt(math.pow(self.x,2) + math.pow(self.y,2) + math.pow(self.z,2)),10)

    def normalized(self):
        return Vector3(self.x/self.getMagnitude(),self.y/self.getMagnitude(),self.z/self.getMagnitude())
    
    
