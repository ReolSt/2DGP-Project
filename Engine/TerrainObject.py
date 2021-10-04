import pico2d

from .TerrainSprite import *
from .GameObject import *

class TerrainObject(GameObject):
    def __init__(self, parent, spriteName):
        super().__init__(parent)
        self.sprites.append(TerrainSprite(self.transform, spriteName))