from Engine.GameObject import GameObject
from Engine.EntitySprite import EntitySprite
from Engine.TerrainSprite import TerrainSprite
from Engine.RigidBody import RigidBody
from Engine.AudioMixer import *

import os
if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from .ColliderCategories import *
else:
    from Entities.ColliderCategories import *

class MysteryBlock(GameObject):
    def __init__(self, parent, colorType=1):
        super().__init__(parent)

        sprite = EntitySprite(self, "MysteryBlock" + str(colorType))

        spriteWidth = sprite.width
        spriteHeight = sprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        sprite.transform.translate(xOffset, yOffset)
        self.addSprite(sprite)

        self.rigidBody = RigidBody(self)
        self.rigidBody.vertices = [(0, 0), (spriteWidth, 0), (spriteWidth, spriteHeight), (0, spriteHeight)]
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
