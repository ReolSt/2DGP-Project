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

class EntitySprite(Sprite):
    Map = SpriteMap(
        pico2d.load_image(Settings().sprite['EntitySpritePath']),
        SpriteIndexParser(Settings().sprite['EntitySpriteIndexPath']).indices)

    def __init__(self, parent, spriteName):
        super().__init__(parent, EntitySprite.Map, spriteName)