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

class TerrainSprite(Sprite):
    Map = None

    def __init__(self, parent, spriteName):
        if TerrainSprite.Map is None:
            settings = Settings()
            TerrainSprite.Map = SpriteMap(
                pico2d.load_image(settings.sprite['TerrainSpritePath']),
                SpriteIndexParser(settings.sprite['TerrainSpriteIndexPath']).indices)

        super().__init__(parent, TerrainSprite.Map, spriteName)