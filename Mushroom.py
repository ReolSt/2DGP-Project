from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.BoxCollider import *

class Mushroom(GameObject):
    def __init__(self, parent, width=3, height=3):
        assert width >= 3 and width % 2 and height >= 1, "Impossible mushroom height : ({}, {})".format(width, height)
        super().__init__(parent)

        referenceSprite = TerrainSprite(self, "MushroomPillar1")
        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        objectWidth = spriteWidth * width
        objectHeight = spriteHeight * height

        xOffset = objectWidth / 2
        yOffset = spriteHeight / 2

        for i in range(height - 2):
            pillar = TerrainSprite(self, "MushroomPillar2")
            pillar.transform.translate(xOffset, yOffset)
            self.sprites.append(pillar)

            yOffset += pillar.height

        if height >= 2:
            pillarTop = TerrainSprite(self, "MushroomPillar1")
            pillarTop.transform.translate(xOffset, yOffset)
            self.sprites.append(pillarTop)

            yOffset += pillarTop.height


        xOffset = spriteWidth / 2

        roofLeft = TerrainSprite(self, "MushroomRoof1")
        roofLeft.transform.translate(xOffset, yOffset)
        self.sprites.append(roofLeft)

        xOffset += spriteWidth

        for i in range(width - 2):
            roof = TerrainSprite(self, "MushroomRoof2")
            roof.transform.translate(xOffset, yOffset)
            self.sprites.append(roof)

            xOffset += spriteWidth

        roofRight = TerrainSprite(self, "MushroomRoof3")
        roofRight.transform.translate(xOffset, yOffset)
        self.sprites.append(roofRight)

        collider = BoxCollider(self, objectWidth, spriteHeight)
        collider.transform.translate(objectWidth / 2, objectHeight - spriteHeight / 2)
        collider.setTag("Floor")

        self.addCollider(collider)

