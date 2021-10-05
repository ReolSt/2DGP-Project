from Engine.GameObject import *
from Engine.TerrainSprite import *

class Grass(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        left = TerrainSprite(self.transform, "Grass1")
        center = TerrainSprite(self.transform, "Grass2")
        right = TerrainSprite(self.transform, "Grass3")

        left.transform.translate(-left.width, 0)
        right.transform.translate(right.width, 0)

        self.sprites.append(left)
        self.sprites.append(center)
        self.sprites.append(right)