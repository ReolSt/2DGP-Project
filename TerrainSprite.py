import pico2d

from Settings import *

from Sprite import *
from SpriteMap import *
from SpriteIndexParser import *

class TerrainSprite(Sprite):
    Map = SpriteMap(
        pico2d.load_image(Settings().sprite['TerrainSpritePath']),
        SpriteIndexParser(Settings().sprite['TerrainSpriteIndexPath']).indices)

    def __init__(self, parent, spriteName):
        super().__init__(parent, TerrainSprite.Map, spriteName)