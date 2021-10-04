import pico2d

from .Settings import *

from .Sprite import *
from .SpriteMap import *
from .SpriteIndexParser import *

class TextSprite(Sprite):
    Settings = Settings()

    Map = SpriteMap(
        pico2d.load_image(Settings.sprite['FontSpritePath']),
        SpriteIndexParser(Settings.sprite['FontSpriteIndexPath']).indices)

    def __init__(self, parent, ch=''):
        assert(len(ch) <= 1)

        super().__init__(parent, TextSprite.Map, ch)