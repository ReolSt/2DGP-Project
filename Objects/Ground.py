from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.RigidBody import *

class Ground(GameObject):
    def __init__(self, parent, width=1, height=1, colorType=1):
        assert width >= 1 and height >= 1, "[Ground] Impossible size: ({}, {})".format(width, height)

        super().__init__(parent)

        self.width = width
        self.height = height

        sprite = TerrainSprite(self.transform, "Ground" + str(colorType))
        spriteWidth = sprite.width
        spriteHeight = sprite.height

        for y in range(height):
            for x in range(width):
                currentSprite = TerrainSprite(self.transform, "Ground" + str(colorType))
                currentSprite.transform.translate(
                    spriteWidth / 2 + x * spriteWidth, spriteHeight / 2 + y * spriteHeight)
                self.addSprite(currentSprite)        

        objectWidth = spriteWidth * width
        objectHeight = spriteHeight * height

        self.rigidBody = RigidBody(self)
        self.rigidBody.vertices = [(0, 0), (objectWidth, 0), (objectWidth, objectHeight), (0, objectHeight)]
        self.rigidBody.bodyType = "STATIC"
        self.rigidBody.filter = 0b1