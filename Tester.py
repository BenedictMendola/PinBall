import VectorMath
import Vector3
import Transform

def printVector(vector: Vector3.Vector3):
    print(vector.x,vector.y,vector.z)


vect1 = Vector3.Vector3(14,3,5)
vect2 = Vector3.Vector3(1,1,1)
vect3 = Vector3.Vector3(1,1,1)
transform1 = Transform.Transform(vect1,vect2,vect3)

# #vect3 = VectorMath.add(vect1,vect2)
# vect3 = VectorMath.div(vect1,vect2)
# print(vect3.x,vect3.y,vect3.z)
# print(vect3.getMagnitude())
# vect3 = vect3.normalized()
# print(vect3.x,vect3.y,vect3.z)
# print(vect3.getMagnitude())
# print(vect3.getMagnitude() == 1)

printVector(transform1.position)

transform1.position = VectorMath.add(transform1.position,vect3)
printVector(transform1.position)
