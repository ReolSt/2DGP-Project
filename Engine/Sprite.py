import pico2d

from .Transform import *
from .GameObject import *

class Sprite:
    def __init__(self, parent, spriteMap, spriteName):
        """
        Parameters
        ----------
        parent : GameObject or Transform
            DESCRIPTION.
        spriteMap : SpriteMap
            SpriteMap for loading sprite by name.
        spriteName : str
            DESCRIPTION.

        Returns
        -------
        None.

        """
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

    def render(self, camera):
        """
        Returns
        -------
        None.

        Notes
        -------
        render itself.

        """

        position = camera.translate(self.transform.position)
        rotation = camera.rotate(self.transform.rotation)
        scale = camera.scale(self.transform.scale)

        if position.x - self.width / 2 > 800 or \
           position.x + self.width / 2 < 0:
               return

        if position.y - self.height / 2 > 800 or \
           position.y + self.height / 2 < 0:
               return

        flipString = ''
        flipString += 'h' if self.transform.flip.x else ''
        flipString += 'v' if self.transform.flip.y else ''

        self.image.clip_composite_draw(
            self.left, self.bottom, self.width, self.height,
            rotation, flipString, position.x, position.y,
            self.width * scale.x, self.height * scale.y)