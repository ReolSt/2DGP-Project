from Engine.GameObject import *
from Engine.TerrainSprite import *

class Cloud(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        bottomLeft = TerrainSprite(self.transform, "CloudBottom1")
        bottomCenter = TerrainSprite(self.transform, "CloudBottom2")
        bottomRight = TerrainSprite(self.transform, "CloudBottom3")

        bottomLeft.transform.translate(-bottomLeft.width, 0)
        bottomRight.transform.translate(bottomRight.width, 0)

        topLeft = TerrainSprite(self.transform, "CloudTop1")
        topCenter = TerrainSprite(self.transform, "CloudTop2")
        topRight = TerrainSprite(self.transform, "CloudTop3")

        topLeft.transform.translate(-topLeft.width, topLeft.height)
        topCenter.transform.translate(0, topCenter.height)
        topRight.transform.translate(topRight.width, topLeft.height)

        self.sprites.append(bottomLeft)
        self.sprites.append(bottomCenter)
        self.sprites.append(bottomRight)

        self.sprites.append(topLeft)
        self.sprites.append(topCenter)
        self.sprites.append(topRight)