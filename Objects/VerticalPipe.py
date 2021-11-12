from Engine.GameObject import GameObject
from Engine.TerrainSprite import TerrainSprite
from Engine.RigidBody import RigidBody

import pymunk

class VerticalPipe(GameObject):
    def __init__(self, parent, height=2):
        assert height >= 1, "[VerticalPipe] Impossible height : {}".format(height)
        super().__init__(parent)

        referenceSprite = TerrainSprite(self, "VerticalPipeEntrance1")
        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        for h in range(height - 1):
            pillarLeft = TerrainSprite(self, "VerticalPipePillar1")
            pillarRight = TerrainSprite(self, "VerticalPipePillar2")

            pillarLeft.transform.translate(xOffset, yOffset)
            pillarRight.transform.translate(xOffset + spriteWidth, yOffset)

            yOffset += pillarLeft.height

            self.addSprite(pillarLeft)
            self.addSprite(pillarRight)

        entranceLeft = TerrainSprite(self, "VerticalPipeEntrance1")
        entranceRight = TerrainSprite(self, "VerticalPipeEntrance2")

        entranceLeft.transform.translate(xOffset, yOffset)
        entranceRight.transform.translate(xOffset + spriteWidth, yOffset)

        self.addSprite(entranceLeft)
        self.addSprite(entranceRight)

        objectWidth = spriteWidth * 2
        objectHeight = spriteHeight * height

        body = pymunk.Body()

        shape = pymunk.Poly(body, [(0, 0), (objectWidth, 0), (objectWidth, objectHeight), (0, objectHeight)])

        self.rigidBody = RigidBody(self, body, shape)
        self.rigidBody.bodyType = RigidBody.static
        self.rigidBody.filter = 0b1
        self.rigidBody.elasticity = 0