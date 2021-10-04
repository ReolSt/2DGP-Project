from .Settings import *

from .EntitySprite import *
from .GameObject import *

class EntityObject(GameObject):
    def __init__(self, parent, spriteName):
        super().__init__(parent)
        self.sprites.append(EntitySprite(self.transform, spriteName))