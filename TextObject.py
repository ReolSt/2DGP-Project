from Sprite import *
from GameObject import *

class TextObject(GameObject):
    def __init__(self, parent, spriteMap, text="", spacing=1):
        super().__init__(parent)
        self.text = text
        self.spacing = spacing

        xOffset = 0
        for ch in self.text:
            if ch == " ":
                ch = "SPACE"
            sprite = Sprite(spriteMap, ch, self.transform)
            sprite.transform.position.x += sprite.width + self.spacing

            self.sprites.append(sprite)
            xOffset += sprite.width
