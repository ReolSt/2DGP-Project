from Engine.GameObject import *
from Engine.TerrainSprite import *

class Tree(GameObject):
    def __init__(self, parent, height=3):
        assert height >= 2, "Impossible tree height : {}".format(height)

        super().__init__(parent)

        crownTop = TerrainSprite(self, "TreeCrownTop")
        crownBottom = TerrainSprite(self, "TreeCrownBottom")

        referenceSprite = crownTop
        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        self.addSprite(crownTop)
        self.addSprite(crownBottom)

        for i in range(height - 2):
            truck = TerrainSprite(self, "TreeTruck")
            self.addSprite(truck)

        for i in range(len(self.sprites) - 1, -1, -1):
            self.sprites[i].transform.translate(
                xOffset, yOffset + spriteHeight * (len(self.sprites) - i - 1))

