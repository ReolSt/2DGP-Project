from Engine.GameObject import *
from Engine.TerrainSprite import *

class Mushroom(GameObject):
    def __init__(self, parent, height=3):
        assert height >= 1, "Impossible mushroom height : {}".format(height)
        super().__init__(parent)

        referenceSprite = TerrainSprite(self, "MushroomPillar1")
        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        for i in range(height - 2):
            pillar = TerrainSprite(self, "MushroomPillar2")
            pillar.transform.translate(xOffset + spriteWidth, yOffset)
            self.sprites.append(pillar)

            yOffset += pillar.height

        if height >= 2:
            pillarTop = TerrainSprite(self, "MushroomPillar1")
            pillarTop.transform.translate(xOffset + spriteWidth, yOffset)
            self.sprites.append(pillarTop)

            yOffset += pillarTop.height


        roofLeft = TerrainSprite(self, "MushroomRoof1")
        roofCenter = TerrainSprite(self, "MushroomRoof2")
        roofRight = TerrainSprite(self, "MushroomRoof3")

        roofLeft.transform.translate(xOffset, yOffset)
        roofCenter.transform.translate(xOffset + spriteWidth, yOffset)
        roofRight.transform.translate(xOffset + spriteWidth * 2, yOffset)

        self.sprites.append(roofLeft)
        self.sprites.append(roofCenter)
        self.sprites.append(roofRight)

