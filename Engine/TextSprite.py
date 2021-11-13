import pico2d

import os
if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Settings import Settings
    from Sprite import Sprite
    from SpriteMap import SpriteMap
    from SpriteIndexParser import SpriteIndexParser
else:
    from .Settings import Settings
    from .Sprite import Sprite
    from .SpriteMap import SpriteMap
    from .SpriteIndexParser import SpriteIndexParser

class TextSprite(Sprite):
    Map = None

    def __init__(self, parent, ch=''):
        if TextSprite.Map is None:
            settings = Settings()
            TextSprite.Map = SpriteMap(
                pico2d.load_image(settings.sprite['FontSpritePath']),
                SpriteIndexParser(settings.sprite['FontSpriteIndexPath']).indices)

        super().__init__(parent, TextSprite.Map, ch)