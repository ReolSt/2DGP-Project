import pico2d

import os
if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Settings import *
    from Sprite import *
    from SpriteMap import *
    from SpriteIndexParser import *
else:
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