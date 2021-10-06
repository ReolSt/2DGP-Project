from Engine.GameObject import *
from Engine.TerrainSprite import *

class Flagpole(GameObject):
    def __init__(self, parent, height=10):
        assert height >= 3, "Invalid flagpole height : {}".format(height)

        super().__init__(parent)

        ball = TerrainSprite(self, "FlagpoleBall")

        spriteWidth = ball.width
        spriteHeight = ball.height

        yOffset = spriteHeight / 2

        for i in range(height - 2):
            pole = TerrainSprite(self, "FlagpolePole")
            pole.transform.translate(spriteWidth * 3 / 2, yOffset)

            self.sprites.append(pole)

            yOffset += spriteWidth

        flagLeft = TerrainSprite(self, "FlagpoleFlag1")
        flagRight = TerrainSprite(self, "FlagpoleFlag2")

        flagLeft.transform.translate(spriteWidth / 2, yOffset)
        flagRight.transform.translate(spriteWidth * 3 / 2, yOffset)

        self.sprites.append(flagLeft)
        self.sprites.append(flagRight)

        yOffset += spriteWidth

        ball.transform.translate(spriteWidth * 3 / 2, yOffset)

        self.sprites.append(ball)
