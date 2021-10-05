from Engine.TerrainSprite import *
from Engine.GameObject import *
class Mountain(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        top = TerrainSprite(self.transform, "MountainTop")
        spriteWidth = top.width
        spriteHeight = top.height

        top.transform.translate(0, spriteHeight)

        bottomLeft = TerrainSprite(self.transform, "MountainBottom1")
        bottomLeft.transform.translate(-spriteWidth, 0)

        bottomCenter = TerrainSprite(self.transform, "MountainBottom2")
        bottomCenter.transform.translate(0, 0)

        bottomRight = TerrainSprite(self.transform, "MountainBottom3")
        bottomRight.transform.translate(spriteWidth, 0)

        self.sprites.append(top)
        self.sprites.append(bottomLeft)
        self.sprites.append(bottomCenter)
        self.sprites.append(bottomRight)