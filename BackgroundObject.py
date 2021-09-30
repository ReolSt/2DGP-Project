import pico2d

from BackgroundSprite import *
from GameObject import *

class BackgroundObject(GameObject):
    def __init__(self, parent, spriteName):
        super().__init__(parent)
        self.sprites.append(BackgroundSprite(self.transform, spriteName))