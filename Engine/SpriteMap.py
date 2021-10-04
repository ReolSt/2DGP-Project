import pico2d

from .Sprite import *

SPRITE_PATH = "resources/image/sprite/"

class SpriteMap:
    def __init__(self, image, indices):
        self.image = image
        self.indices = {}

        for name in indices:
            current_index = indices[name]
            startX = current_index['startX']
            startY = current_index['startY']
            endX = current_index['endX']
            endY = current_index['endY']

            x = startX
            y = startX
            width = endX - startX + 1
            height = endY - startY + 1

            left = startX
            bottom = self.image.h - endY - 1

            self.indices[name] = {
                'x': x,
                'y': y,
                'width': width,
                'height': height,
                'left': left,
                'bottom': bottom
            }

    def getSpriteImage(self, name):
        spriteIndex = self.indices[name]

        width = spriteIndex['width']
        height = spriteIndex['height']
        left = spriteIndex['left']
        bottom = spriteIndex['bottom']

        return self.image.clip_image(left, bottom, width, height)

    def getSprite(self, name, parent):
        sprite = Sprite(self, name, parent)

        return sprite