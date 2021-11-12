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

class EntitySprite(Sprite):
    Map = None

    def __init__(self, parent, spriteName):
        if EntitySprite.Map is None:
            settings = Settings()
            EntitySprite.Map = SpriteMap(
                pico2d.load_image(settings.sprite['EntitySpritePath']),
                SpriteIndexParser(settings.sprite['EntitySpriteIndexPath']).indices)

        super().__init__(parent, EntitySprite.Map, spriteName)