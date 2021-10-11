import pico2d
import numpy

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

        position = self.transform.position()
        rotation = self.transform.rotation()
        scale = self.transform.scale()
        flip = self.transform.flip()

        cameraPosition = -camera.transform.position()
        cameraRotation = -camera.transform.rotation()
        cameraScale = camera.transform.localScale

        cos = numpy.cos(numpy.deg2rad(cameraRotation))
        sin = numpy.sin(numpy.deg2rad(cameraRotation))

        position *= cameraScale
        position = Vector2(position.x * cos - position.y * sin,
                           position.y * cos + position.x * sin)
        position += cameraPosition

        rotation += cameraRotation
        scale *= cameraScale

        flipString = ''
        flipString += 'h' if flip.x else ''
        flipString += 'v' if flip.y else ''

        self.image.clip_composite_draw(
            self.left, self.bottom, self.width, self.height,
            rotation, flipString, position.x, position.y,
            self.width * scale.x, self.height * scale.y)