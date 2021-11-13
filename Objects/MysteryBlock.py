from Engine.GameObject import GameObject
from Engine.EntitySprite import EntitySprite
from Engine.TerrainSprite import TerrainSprite
from Engine.RigidBody import RigidBody

class MysteryBlock(GameObject):
    def __init__(self, parent, colorType=1):
        super().__init__(parent)

        sprite = EntitySprite(self, "MysteryBlock" + str(colorType))

        spriteWidth = sprite.width
        spriteHeight = sprite.height

        xOffset = spriteWidth / 2
        yOffset = spriteHeight / 2

        sprite.transform.translate(xOffset, yOffset)
        self.addSprite(sprite)

        self.rigidBody = RigidBody(self)
        self.rigidBody.vertices = [(0, 0), (spriteWidth, 0), (spriteWidth, spriteHeight), (0, spriteHeight)]
        self.rigidBody.bodyType = "Static"
        self.rigidBody.filter = 0b1
