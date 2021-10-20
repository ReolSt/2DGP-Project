from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.BoxCollider import *


class Brick(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        sprite = TerrainSprite(self, "Brick")

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