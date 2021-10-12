from Engine.GameObject import *
from Engine.TerrainSprite import *
from Engine.BoxCollider import *

class Ground(GameObject):
    def __init__(self, parent, width, height):
        assert width >= 1 and height >= 1, "Impossible ground size: ({}, {})".format(width, height)

        super().__init__(parent)

        self.width = width
        self.height = height

        sprite = TerrainSprite(self.transform, "Ground")
        spriteWidth = sprite.width
        spriteHeight = sprite.height

        for y in range(height):
            for x in range(width):
                currentSprite = TerrainSprite(self.transform, "Ground")
                currentSprite.transform.translate(
                    spriteWidth / 2 + x * spriteWidth, spriteHeight / 2 + y * spriteHeight)
                self.sprites.append(currentSprite)

        collider = BoxCollider(self,
            spriteWidth * width, spriteHeight * height)
        collider.transform.translate(
            spriteWidth * width / 2, spriteHeight * height / 2)
        collider.setTag("Floor")
        collider.renderMesh = True

        self.addCollider(collider)