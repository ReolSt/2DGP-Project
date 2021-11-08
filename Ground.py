from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.RigidBody import *

import pymunk

class Ground(GameObject):
    def __init__(self, parent, width, height):
        assert width >= 1 and height >= 1, "[Ground] Impossible size: ({}, {})".format(width, height)

        super().__init__(parent)

        self.width = width
        self.height = height

        sprite = TerrainSprite(self.transform, "Ground")
        spriteWidth = sprite.width
        spriteHeight = sprite.height

        for y in range(height):
            for x in range(width):
                currentSprite = TerrainSprite(self.transform, "Ground")
                currentSprite.transform.translate(
                    spriteWidth / 2 + x * spriteWidth, spriteHeight / 2 + y * spriteHeight)
                self.addSprite(currentSprite)        

        objectWidth = spriteWidth * width
        objectHeight = spriteHeight * height

        body = pymunk.Body()

        shape = pymunk.Poly(body, [(0, 0), (objectWidth, 0), (objectWidth, objectHeight), (0, objectHeight)])

        self.rigidBody = RigidBody(self, body, shape)
        self.rigidBody.bodyType = "STATIC"
        self.rigidBody.filter = pymunk.ShapeFilter(categories=0b1)
        self.rigidBody.elasticity = 0
        self.rigidBody.friction = 1