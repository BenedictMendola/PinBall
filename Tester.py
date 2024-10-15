import VectorMath
import Vector3
import Transform


vect1 = Vector3.Vector3(-20,3,5)
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

print(transform1.position.x,transform1.position.y,transform1.position.z)
transform1.position = Vector3.Vector3(0,0,0)
print(transform1.position.x,transform1.position.y,transform1.position.z)