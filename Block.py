from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.BoxCollider import *

class Block(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        assert width >= 1 and height >= 1, "[Block] Impossible size : ({}, {})".format(width, height)

        spriteWidth = sprite.width
        spriteHeight = sprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        sprite.transform.translate(xOffset, yOffset)
        self.addSprite(sprite)

        objectWidth = spriteWidth * width
        objectHeight = spriteHeight * height

        body = pymunk.Body()
        shape = pymunk.Poly(body, [(0, 0), (objectWidth, 0), (objectWidth, objectHeight), (0, objectHeight)])

        self.rigidBody = RigidBody(self, body, shape)
        self.rigidBody.bodyType = "Static"
        self.rigidBody.filter = 0b1
