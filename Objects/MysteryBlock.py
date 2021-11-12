from Engine.GameObject import *
from Engine.EntitySprite import *
from Engine.TerrainSprite import *
from Engine.RigidBody import *

import pymunk

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

        body = pymunk.Body()
        shape = pymunk.Poly(body, [(0, 0), (spriteWidth, 0), (spriteWidth, spriteHeight), (0, spriteHeight)])

        self.rigidBody = RigidBody(self, body, shape)
        self.rigidBody.bodyType = "Static"
        self.rigidBody.filter = 0b1
