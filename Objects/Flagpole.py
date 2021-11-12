from Engine.GameObject import GameObject
from Engine.TerrainSprite import TerrainSprite
from Engine.RigidBody import RigidBody

import pymunk

class Flagpole(GameObject):
    def __init__(self, parent, height=10):
        assert height >= 3, "[Flagpole] Invalid height : {}".format(height)

        super().__init__(parent)

        ball = TerrainSprite(self, "FlagpoleBall")

        referenceSprite = ball

        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        objectWidth = spriteWidth * 2
        objectHeight = spriteHeight * height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        for i in range(height - 2):
            pole = TerrainSprite(self, "FlagpolePole")
            pole.transform.translate(-xOffset + spriteWidth, yOffset)

            self.addSprite(pole)

            yOffset += spriteWidth

        flagLeft = TerrainSprite(self, "FlagpoleFlag1")
        flagRight = TerrainSprite(self, "FlagpoleFlag2")

        flagLeft.transform.translate(-xOffset, yOffset)
        flagRight.transform.translate(-xOffset + spriteWidth, yOffset)

        self.addSprite(flagLeft)
        self.addSprite(flagRight)

        yOffset += spriteWidth

        ball.transform.translate(-xOffset + spriteWidth, yOffset)

        self.addSprite(ball)

        body = pymunk.Body()
        shape = pymunk.Poly(body, [(0, 0), (objectWidth / 2, 0), (objectWidth / 2, objectHeight), (0, objectHeight)])

        self.rigidBody = RigidBody(self, body, shape)
        self.rigidBody.bodyType = "Static"
        self.rigidBody.filter = 0b10