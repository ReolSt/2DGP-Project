from Engine.GameObject import GameObject
from Engine.TerrainSprite import TerrainSprite

class Background(GameObject):
    def __init__(self, parent, width, height, spriteName):
        assert width >= 0 and height >= 0, "[Background] Invalid size : ({}, {})".format(width, height)

        super().__init__(parent)

        sprite = TerrainSprite(self, spriteName)
        sprite.transform.translate(sprite.width / 2, sprite.height / 2)

        self.addSprite(sprite)

        self.transform.setLocalScale(width / sprite.width, height / sprite.height)

        self.width = width
        self.height = height

    def update(self, deltaTime):
        super().update(deltaTime)
        self.sprites[0].transform.setPosition(self.width / 2, self.height / 2)
        self.transform.setScale(800 / self.sprites[0].width, 600 / self.sprites[0].height)