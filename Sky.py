from Engine.GameObject import *
from Engine.TerrainSprite import *

class Sky(GameObject):
    def __init__(self, parent, width, height):
        assert width >= 0 and height >= 0, "Sky size is negative : ({}, {})".format(width, height)

        super().__init__(parent)

        sprite = TerrainSprite(self, "Sky")
        sprite.transform.translate(sprite.width / 2, sprite.height / 2)

        self.sprites.append(sprite)

        self.transform.setScale(width / sprite.width, height / sprite.height)