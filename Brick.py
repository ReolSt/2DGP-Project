from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.BoxCollider import *


class Brick(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        assert width >= 1 and height >= 1, "[Brick] Impossible size : ({}, {})".format(width, height)

        spriteWidth = sprite.width
        spriteHeight = sprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        sprite.transform.translate(xOffset, yOffset)
        self.addSprite(sprite)

        collider = BoxCollider(self, spriteWidth, spriteHeight)
        collider.transform.translate(xOffset, yOffset)
        collider.tag = "Floor"
        self.addCollider(collider)