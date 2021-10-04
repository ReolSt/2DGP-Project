from .Settings import *

from .Sprite import *
from .SpriteMap import *
from .SpriteIndexParser import *

class BackgroundSprite(Sprite):
    Settings = Settings()

    Map = SpriteMap(
        pico2d.load_image(Settings.sprite['BackgroundSpritePath']),
        SpriteIndexParser(Settings.sprite['BackgroundSpriteIndexPath']).indices)

    def __init__(self, parent, spriteName):
        super().__init__(parent, BackgroundSprite.Map, spriteName)