import pico2d

from Settings import *

from Sprite import *
from SpriteMap import *
from SpriteIndexParser import *

class EntitySprite(Sprite):
    Map = SpriteMap(
        pico2d.load_image(Settings().sprite['EntitySpritePath']),
        SpriteIndexParser(Settings().sprite['EntitySpriteIndexPath']).indices)

    def __init__(self, parent, spriteName):
        super().__init__(parent, EntitySprite.Map, spriteName)