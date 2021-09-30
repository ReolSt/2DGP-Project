import pico2d

from Transform import *
from GameObject import *

class Sprite:
    def __init__(self, parent, spriteMap, spriteName):
        self.image = spriteMap.image
        self.spriteName = spriteName
        self.spriteIndex = spriteMap.indices[spriteName]

        if isinstance(parent, GameObject):
            self.transform = Transform(parent.transform)
        else:
            self.transform = Transform(parent)

    def render(self):
        width = self.spriteIndex['width']
        height = self.spriteIndex['height']
        left = self.spriteIndex['left']
        bottom = self.spriteIndex['bottom']

        x, y = self.transform.position()
        rotation = self.transform.rotation()
        scale = self.transform.scale()
        flip = self.transform.flip()

        flipString = ''
        flipString += 'h' if flip[0] else ''
        flipString += 'v' if flip[1] else ''

        self.image.clip_composite_draw(left, bottom, width, height,
            rotation, flipString, x, y, width * scale[0], height * scale[1])