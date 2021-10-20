from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.BoxCollider import *

class VerticalPipe(GameObject):
    def __init__(self, parent, height=2):
        assert height >= 1, "Impossible vertical pipe height : {}".format(height)
        super().__init__(parent)

        referenceSprite = TerrainSprite(self, "VerticalPipeEntrance1")
        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        for h in range(height - 1):
            pillarLeft = TerrainSprite(self, "VerticalPipePillar1")
            pillarRight = TerrainSprite(self, "VerticalPipePillar2")

            pillarLeft.transform.translate(xOffset, yOffset)
            pillarRight.transform.translate(xOffset + spriteWidth, yOffset)

            yOffset += pillarLeft.height

            self.addSprite(pillarLeft)
            self.addSprite(pillarRight)

        entranceLeft = TerrainSprite(self, "VerticalPipeEntrance1")
        entranceRight = TerrainSprite(self, "VerticalPipeEntrance2")

        entranceLeft.transform.translate(xOffset, yOffset)
        entranceRight.transform.translate(xOffset + spriteWidth, yOffset)

        self.addSprite(entranceLeft)
        self.addSprite(entranceRight)

        collider = BoxCollider(self, spriteWidth * 2, spriteHeight * height)
        collider.transform.translate(spriteWidth, spriteHeight * height / 2)
        collider.setTag("Floor")

        self.addCollider(collider)