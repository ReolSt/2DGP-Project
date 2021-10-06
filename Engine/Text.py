import pico2d

from .TextSprite import *
from .EntitySprite import *
from .GameObject import *

class Text(GameObject):
    def __init__(self, parent, text="", spacing=1):
        super().__init__(parent)
        self.text = text
        self.spacing = spacing
        self.setText(text)

    def setText(self, text):
        self.text = text
        self.sprites.clear()

        xOffset = 0.0
        for ch in self.text:
            if ch == " ":
                ch = "SPACE"
            sprite = TextSprite(self.transform, ch)

            sprite.transform.localPosition.x += xOffset

            self.sprites.append(sprite)

            xOffset += sprite.spriteIndex['width'] + self.spacing
