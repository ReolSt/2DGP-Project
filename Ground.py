from Engine.GameObject import *
from Engine.TerrainSprite import *

class Ground(GameObject):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.width = width
        self.height = height

        for y in range(height):
            for x in range(width):
                sprite = TerrainSprite(self.transform, "Ground")