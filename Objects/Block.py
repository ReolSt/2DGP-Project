from Engine.GameObject import GameObject
from Engine.TerrainSprite import TerrainSprite
from Engine.RigidBody import RigidBody

class Block(GameObject):
    def __init__(self, parent, width=1, height=1, colorType=1):
        super().__init__(parent)

        assert width >= 1 and height >= 1, "[Block] Impossible size : ({}, {})".format(width, height)

        referenceSprite = TerrainSprite(self, "Block" + str(colorType))

        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        for y in range(height):
            for x in range(width):
                sprite = TerrainSprite(self, "Block" + str(colorType))

                sprite.transform.translate(xOffset + spriteWidth * x, yOffset + spriteHeight * y)
                self.addSprite(sprite)

        objectWidth = spriteWidth * width
        objectHeight = spriteHeight * height

        self.rigidBody = RigidBody(self)
        self.rigidBody.vertices = [(0, 0), (objectWidth, 0), (objectWidth, objectHeight), (0, objectHeight)]
        self.rigidBody.bodyType = "Static"
        self.rigidBody.filter = 0b1
