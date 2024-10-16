import GameObject
import Vector3

def makeRedCircle(startingPos: Vector3.Vector3, vectorAngle:Vector3.Vector3,initVelocity: Vector3.Vector3,angularVelocity:int,mass:int):
    redCircle = GameObject.GameObject("RedCircle",startingPos,Vector3.Vector3(3,3,1),vectorAngle)
    redCircle.addRidgidBody(initVelocity,angularVelocity,mass)
    redCircle.addSpriteRenderer('Assets\RedCircle1.png')
    redCircle.addBoxCollider()
    return redCircle

def makeBlueBoxHoriz(startingPos: Vector3.Vector3,vectorAngle: Vector3.Vector3):
    colisionBox = GameObject.GameObject("Collison Box",startingPos,Vector3.Vector3(3,3,1),vectorAngle)
    colisionBox.addSpriteRenderer('Assets\Rectangle.png')
    colisionBox.addBoxCollider()
    return colisionBox
def makeBlueBoxVert(startingPos: Vector3.Vector3,vectorAngle: Vector3.Vector3):
    colisionBox = GameObject.GameObject("Collison Box",startingPos,Vector3.Vector3(3,3,1),vectorAngle)
    colisionBox.addSpriteRenderer('Assets\Rectangle1.png')
    colisionBox.addBoxCollider()
    return colisionBox