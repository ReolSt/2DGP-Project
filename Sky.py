from Engine.GameObject import *
from Engine.TerrainSprite import *

class Sky(GameObject):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        sprite = TerrainSprite(self, "Sky")
        self.sprites.append(sprite)

        self.transform.setScale(width / sprite.width, height / sprite.height)