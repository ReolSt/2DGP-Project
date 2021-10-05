import pico2d

from .Sprite import *

SPRITE_PATH = "resources/image/sprite/"

class SpriteMap:
    def __init__(self, image, indices):
        """
        Parameters
        ----------
        image : SDL_Image
            DESCRIPTION.
        indices : dictionary
            The dictionary has 4 keys('startX', 'startY', 'endX', 'endY')

        Returns
        -------
        None.

        """

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
        """

        Parameters
        ----------
        name : str
            The name of sprite.

        Returns
        -------
        TYPE
            SDL_Image.

        """
        spriteIndex = self.indices[name]

        width = spriteIndex['width']
        height = spriteIndex['height']
        left = spriteIndex['left']
        bottom = spriteIndex['bottom']

        return self.image.clip_image(left, bottom, width, height)

    def getSprite(self, name, parent):
        """

        Parameters
        ----------
        name : str
            DESCRIPTION.
        parent : Gameobject or Transform
            DESCRIPTION.

        Returns
        -------
        sprite : Sprite
            DESCRIPTION.

        """

        sprite = Sprite(self, name, parent)

        return sprite