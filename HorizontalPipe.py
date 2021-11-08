from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.BoxCollider import *

class HorizontalPipe(GameObject):
    def __init__(self, parent, width=4, height=3):
        assert width >= 3 and height >=3, "[HorizontalPipe] Impossible size : ({}, {})".format(width, height)

        super().__init__(parent)

        referenceSprite = TerrainSprite(self, "LeftPipeEntrance1")
        spriteWidth = referenceSprite.width
        spriteHeight = referenceSprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        entranceLeftTop = TerrainSprite(self, "LeftPipeEntrance1")
        entranceLeftBottom = TerrainSprite(self, "LeftPipeEntrance2")

        entranceLeftTop.transform.translate(xOffset, yOffset + spriteHeight)
        entranceLeftBottom.transform.translate(xOffset, yOffset)

        self.addSprite(entranceLeftTop)
        self.addSprite(entranceLeftBottom)

        xOffset += spriteWidth

        for i in range(width - 3):
            pillarLeftTop = TerrainSprite(self, "LeftPipePillar1")
            pillarLeftBottom = TerrainSprite(self, "LeftPipePillar2")

            pillarLeftTop.transform.translate(xOffset, yOffset + spriteHeight)
            pillarLeftBottom.transform.translate(xOffset, yOffset)

            self.addSprite(pillarLeftTop)
            self.addSprite(pillarLeftBottom)

            xOffset += spriteWidth

        # horizontal pillar

        pillarBottomLeft = TerrainSprite(self, "LeftPipeConnect2")
        pillarBottomRight = TerrainSprite(self, "VerticalPipePillar2")

        pillarBottomLeft.transform.translate(xOffset, yOffset)
        pillarBottomRight.transform.translate(xOffset + spriteWidth, yOffset)

        self.addSprite(pillarBottomLeft)
        self.addSprite(pillarBottomRight)

        yOffset += spriteHeight

        pillarTopLeft = TerrainSprite(self, "LeftPipeConnect1")
        pillarTopRight = TerrainSprite(self, "VerticalPipePillar2")

        pillarTopLeft.transform.translate(xOffset, yOffset)
        pillarTopRight.transform.translate(xOffset + spriteWidth, yOffset)

        yOffset += spriteHeight

        self.addSprite(pillarTopLeft)
        self.addSprite(pillarTopRight)

        for i in range(height - 3):
            pillarLeft = TerrainSprite(self, "VerticalPipePillar1")
            pillarRight = TerrainSprite(self, "VerticalPipePillar2")

            pillarLeft.transform.translate(xOffset, yOffset)
            pillarRight.transform.translate(xOffset + spriteWidth, yOffset)

            yOffset += spriteHeight

            self.addSprite(pillarLeft)
            self.addSprite(pillarRight)

        pillarEntranceLeft = TerrainSprite(self, "VerticalPipeEntrance1")
        pillarEntranceRight = TerrainSprite(self, "VerticalPipeEntrance2")

        pillarEntranceLeft.transform.translate(xOffset, yOffset)
        pillarEntranceRight.transform.translate(xOffset + spriteWidth, yOffset)

        yOffset += spriteHeight

        self.addSprite(pillarEntranceLeft)
        self.addSprite(pillarEntranceRight)

        leftWidth = spriteWidth * (width - 2)
        leftHeight = spriteHeight * 2

        colliderLeft = BoxCollider(self, leftWidth, leftHeight)
        colliderLeft.transform.translate(leftWidth / 2, leftHeight / 2)
        colliderLeft.tag = "Floor"

        verticalWidth = spriteWidth * 2
        verticalHeight = spriteHeight * height

        colliderVertical = BoxCollider(self, verticalWidth, verticalHeight)
        colliderVertical.transform.translate(leftWidth + verticalWidth / 2, verticalHeight / 2)
        colliderVertical.tag = "Floor"

        self.addCollider(colliderLeft)
        self.addCollider(colliderVertical)

