import Vector3

def add(vector1: Vector3.Vector3, vector2: Vector3.Vector3):
    x = vector1.x + vector2.x
    y = vector1.y + vector2.y
    z = vector1.z + vector2.z
    return Vector3.Vector3(x,y,z)
def div(vector1:Vector3.Vector3,vector2: Vector3.Vector3):
    x = vector1.x/vector2.x
    y = vector1.y/vector2.y
    z = vector1.z/vector2.z
    return Vector3.Vector3(x,y,z)
def mul(vector1: Vector3.Vector3,vector2: Vector3.Vector3):
    x = vector1.x * vector2.x
    y = vector1.y * vector2.y
    z = vector1.z * vector2.z
    return Vector3.Vector3(x,y,z)
