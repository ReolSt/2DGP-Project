from Engine.GameObject import *
from Engine.TerrainSprite import *

class Cloud(GameObject):
    def __init__(self, parent, width=2):
        assert width >= 2, "Impossible Cloud width : {}".format(width)

        super().__init__(parent)

        bottomLeft = TerrainSprite(self.transform, "CloudBottom1")
        topLeft = TerrainSprite(self.transform, "CloudTop1")

        referenceSprite = bottomLeft
        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        bottomLeft.transform.translate(xOffset, yOffset)
        topLeft.transform.translate(xOffset, yOffset + spriteHeight)

        xOffset += spriteWidth

        self.sprites.append(bottomLeft)
        self.sprites.append(topLeft)

        for x in range(width - 2):
            bottom = TerrainSprite(self, "CloudBottom2")
            top = TerrainSprite(self, "CloudTop2")

            bottom.transform.translate(xOffset, yOffset)
            top.transform.translate(xOffset, yOffset + spriteHeight)

            self.sprites.append(bottom)
            self.sprites.append(top)

            xOffset += spriteWidth

        bottomRight = TerrainSprite(self.transform, "CloudBottom3")
        topRight = TerrainSprite(self.transform, "CloudTop3")

        bottomRight.transform.translate(xOffset, yOffset)
        topRight.transform.translate(xOffset, yOffset + spriteHeight)

        self.sprites.append(bottomRight)
        self.sprites.append(topRight)