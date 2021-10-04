import pico2d

from .Transform import *
from .GameObject import *

class Sprite:
    def __init__(self, parent, spriteMap, spriteName):
        self.image = spriteMap.image
        self.spriteName = spriteName
        self.spriteIndex = spriteMap.indices[spriteName]

        self.width = self.spriteIndex['width']
        self.height = self.spriteIndex['height']
        self.left = self.spriteIndex['left']
        self.bottom = self.spriteIndex['bottom']

        if isinstance(parent, GameObject):
            self.transform = Transform(parent.transform)
        else:
            self.transform = Transform(parent)

    def render(self):
        x, y = self.transform.position()
        rotation = self.transform.rotation()
        scale = self.transform.scale()
        flip = self.transform.flip()

        flipString = ''
        flipString += 'h' if flip[0] else ''
        flipString += 'v' if flip[1] else ''

        self.image.clip_composite_draw(self.left, self.bottom, self.width, self.height,
            rotation, flipString, x, y, self.width * scale[0], self.height * scale[1])