from Engine.TerrainSprite import *
from Engine.GameObject import *

class VerticalPipe(GameObject):
    def __init__(self, parent, height=2):
        assert height >= 1, "Impossible vertical pipe height : {}".format(height)
        super().__init__(parent)

        referenceSprite = TerrainSprite(self.transform, "VerticalPipeEntrance1")
        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        for h in range(height - 1):
            pillarLeft = TerrainSprite(self.transform, "VerticalPipePillar1")
            pillarRight = TerrainSprite(self.transform, "VerticalPipePillar2")

            pillarLeft.transform.translate(xOffset, yOffset)
            pillarRight.transform.translate(xOffset + spriteWidth, yOffset)

            yOffset += pillarLeft.height

            self.sprites.append(pillarLeft)
            self.sprites.append(pillarRight)

        entranceLeft = TerrainSprite(self.transform, "VerticalPipeEntrance1")
        entranceRight = TerrainSprite(self.transform, "VerticalPipeEntrance2")

        entranceLeft.transform.translate(xOffset, yOffset)
        entranceRight.transform.translate(xOffset + spriteWidth, yOffset)

        self.sprites.append(entranceLeft)
        self.sprites.append(entranceRight)