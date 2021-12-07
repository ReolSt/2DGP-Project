from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.RigidBody import *
from Engine.AudioMixer import *

import os
if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from .ColliderCategories import *
else:
    from Entities.ColliderCategories import *

class BrickUnit(GameObject):
    def __init__(self, parent, colorType=1):
        super().__init__(parent)        

        sprite = TerrainSprite(self, "Brick" + str(colorType))
        self.addSprite(sprite)

        objectWidth = sprite.width
        objectHeight = sprite.height

        xOffset = objectWidth / 2
        yOffset = objectHeight / 2

        sprite.transform.translate(xOffset, yOffset)

        self.rigidBody = RigidBody(self)
        self.rigidBody.vertices = [(0, 0), (objectWidth, 0), (objectWidth, objectHeight), (0, objectHeight)]
        self.rigidBody.bodyType = "KINEMATIC"
        self.rigidBody.filter = 0b1

        self.bumpingTime = 0
        self.bumping = False


    def update(self, deltaTime):
        super().update(deltaTime)

        if self.bumping:
            self.bumpingTime += deltaTime

            if self.bumpingTime >= 100.0:
                self.rigidBody.velocityY = -100

            if self.bumpingTime >= 200.0:
                self.bumping = False
                self.rigidBody.velocityY = 0

                self.transform.setPosition(self.originalPosition)

            return

        bb = self.rigidBody.bb

        for queryInfo in self.rigidBody.space.shape_query(self.rigidBody.shape):
            shape = queryInfo.shape
            contactPoints = queryInfo.contact_point_set.points
            if shape.filter.categories & PLAYER_CATEGORY:
                for contactPoint in contactPoints:
                    point_a = contactPoint.point_a
                    point_b = contactPoint.point_b
                    if bb.left + 2 <= point_a.x <= bb.right - 2 and bb.bottom - 2 <= point_a.y <= bb.bottom:

                        AudioMixer().playWav("Bump")
                        self.bumping = True
                        self.bumpingTime = 0

                        self.originalPosition = self.transform.getPosition()

                        self.rigidBody.velocityY = 100

class Brick(GameObject):
    def __init__(self, parent, width=1, height=1, colorType=1):
        super().__init__(parent)

        assert width >= 1 and height >= 1, "[Brick] Impossible size : ({}, {})".format(width, height)

        referenceSprite = TerrainSprite(self, "Brick" + str(colorType))

        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        for y in range(height):
            for x in range(width):
                brick = BrickUnit(self, colorType)
                brick.transform.translate(spriteWidth * x, spriteHeight * y)

                self.addChild(brick)