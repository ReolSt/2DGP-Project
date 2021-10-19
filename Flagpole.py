from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.BoxCollider import *

class Flagpole(GameObject):
    def __init__(self, parent, height=10):
        assert height >= 3, "Invalid flagpole height : {}".format(height)

        super().__init__(parent)

        ball = TerrainSprite(self, "FlagpoleBall")

        referenceSprite = ball

        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        objectWidth = spriteWidth
        objectHeight = spriteHeight * height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        for i in range(height - 2):
            pole = TerrainSprite(self, "FlagpolePole")
            pole.transform.translate(xOffset + spriteWidth, yOffset)

            self.sprites.append(pole)

            yOffset += spriteWidth

        flagLeft = TerrainSprite(self, "FlagpoleFlag1")
        flagRight = TerrainSprite(self, "FlagpoleFlag2")

        flagLeft.transform.translate(xOffset, yOffset)
        flagRight.transform.translate(xOffset + spriteWidth, yOffset)

        self.sprites.append(flagLeft)
        self.sprites.append(flagRight)

        yOffset += spriteWidth

        ball.transform.translate(xOffset + spriteWidth, yOffset)

        self.sprites.append(ball)

        collider = BoxCollider(self, objectWidth, objectHeight)
        collider.transform.translate(objectWidth * 1.5, objectHeight / 2)

        self.addCollider(collider)