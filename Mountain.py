from Engine.TerrainSprite import *
from Engine.GameObject import *
class Mountain(GameObject):
    def __init__(self, parent, height=2):
        assert 1 <= height <= 3, "Impossible mountain height : {}".format(height)

        super().__init__(parent)

        top = TerrainSprite(self.transform, "MountainTop")

        referenceSprite = top
        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        top.transform.translate(xOffset, yOffset)

        self.addSprite(top)

        if height == 1:
            return

        top.transform.translate(spriteWidth, spriteHeight)

        slopeLeft = TerrainSprite(self.transform, "MountainSlopeLeft")
        slopeLeft.transform.translate(xOffset, yOffset)

        inside = TerrainSprite(self.transform, "MountainInside1")
        inside.transform.translate(xOffset + spriteWidth, yOffset)

        slopeRight = TerrainSprite(self.transform, "MountainSlopeRight")
        slopeRight.transform.translate(xOffset + spriteWidth * 2, yOffset)

        self.addSprite(slopeLeft)
        self.addSprite(inside)
        self.addSprite(slopeRight)

        if height == 2:
            return

        top.transform.translate(spriteWidth, spriteHeight)
        slopeLeft.transform.translate(spriteWidth, spriteHeight)
        inside.transform.translate(spriteWidth, spriteHeight)
        slopeRight.transform.translate(spriteWidth, spriteHeight)

        bottomSlopeLeft = TerrainSprite(self.transform, "MountainSlopeLeft")
        bottomInside1 = TerrainSprite(self.transform, "MountainInside1")
        bottomInside2 = TerrainSprite(self.transform, "MountainInside2")
        bottomInside3 = TerrainSprite(self.transform, "MountainInside3")
        bottomSlopeRight = TerrainSprite(self.transform, "MountainSlopeRight")

        bottomSlopeLeft.transform.translate(xOffset, yOffset)
        bottomInside1.transform.translate(xOffset + spriteWidth, yOffset)
        bottomInside2.transform.translate(xOffset + spriteWidth * 2, yOffset)
        bottomInside3.transform.translate(xOffset + spriteWidth * 3, yOffset)
        bottomSlopeRight.transform.translate(xOffset + spriteWidth * 4, yOffset)

        self.addSprite(bottomSlopeLeft)
        self.addSprite(bottomInside1)
        self.addSprite(bottomInside2)
        self.addSprite(bottomInside3)
        self.addSprite(bottomSlopeRight)

