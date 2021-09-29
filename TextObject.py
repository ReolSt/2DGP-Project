from Sprite import *
from GameObject import *

class TextObject(GameObject):
    def __init__(self, parent, spriteMap, text="", spacing=1):
        super().__init__(parent)
        self.text = text
        self.spacing = spacing

        self.setText(spriteMap, text)

    def setText(self, spriteMap, text):
        self.text = text
        self.sprites.clear()

        xOffset = 0.0
        for ch in self.text:
            if ch == " ":
                ch = "SPACE"
            sprite = Sprite(spriteMap, ch, self.transform)

            sprite.transform.localPosition[0] += xOffset

            self.sprites.append(sprite)

            xOffset += sprite.spriteIndex['width'] + self.spacing
