from Engine.GameObject import GameObject
from Engine.TerrainSprite import TerrainSprite

class Grass(GameObject):
    def __init__(self, parent, width=3):
        assert width >= 2, "Impossible grass width : {}".format(width)

        super().__init__(parent)

        left = TerrainSprite(self.transform, "Grass1")

        referenceSprite = left
        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        left.transform.translate(xOffset, yOffset)
        self.addSprite(left)

        xOffset += spriteWidth

        for i in range(width - 2):
            inside = TerrainSprite(self.transform, "Grass2")
            inside.transform.translate(xOffset, yOffset)
            self.addSprite(inside)

            xOffset += spriteWidth

        right = TerrainSprite(self.transform, "Grass3")
        right.transform.translate(xOffset, yOffset)

        self.addSprite(right)