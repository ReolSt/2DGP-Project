from Engine.TerrainSprite import *
from Engine.GameObject import *
class Mountain(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        spriteTop = TerrainSprite(self.transform, "MountainTop")
        spriteWidth = spriteTop.width
        spriteHeight = spriteTop.height

        spriteTop.transform.translate(0, spriteHeight)

        spriteBottomLeft = TerrainSprite(self.transform, "MountainBottom1")
        spriteBottomLeft.transform.translate(-spriteWidth, 0)

        spriteBottomCenter = TerrainSprite(self.transform, "MountainBottom2")
        spriteBottomCenter.transform.translate(0, 0)

        spriteBottomRight = TerrainSprite(self.transform, "MountainBottom3")
        spriteBottomRight.transform.translate(spriteWidth, 0)

        self.sprites.append(spriteTop)
        self.sprites.append(spriteBottomLeft)
        self.sprites.append(spriteBottomCenter)
        self.sprites.append(spriteBottomRight)