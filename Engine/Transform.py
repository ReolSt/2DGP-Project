import math

import os
if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Vector2 import *
else:
    from .Vector2 import *

class Transform:
    def __init__(self, parent=None, gameObject=None):
        assert isinstance(parent, Transform) or parent is None, "Invalid parameter type: {}".format(parent)

        self.parent = parent
        self.gameObject = gameObject

        self.localPosition = Vector2(0.0, 0.0)
        self.localScale = Vector2(1.0, 1.0)
        self.localFlip = Vector2(False, False)

        self.position = self.localPosition.copy()
        self.scale = self.localScale
        self.flip = self.localFlip

        self.update()

    def update(self):
        self.updateFlip()
        self.updateScale()
        self.updatePosition()

    def getPosition(self) -> Vector2:
        position = self.localPosition.copy()

        if self.parent is not None:
            position *= self.parent.getScale()
            position += self.parent.getPosition()

        return position

    def getScale(self) -> Vector2:
        scale = self.localScale

        if self.parent is not None:
            scale *= self.parent.getScale()

        return scale

    def setPosition(self, *args):
        if len(args) == 1:
            position = args[0]
        elif len(args) == 2:
            position = Vector2(args[0], args[1])

        self.localPosition = position

        if self.parent is not None:
            parentPosition = self.parent.getPosition()
            parentScale = self.parent.getScale()

            if parentScale.x == 0.0:
                return
            if parentScale.y == 0.0:
                return
            
            self.localPosition -= parentPosition

            self.localPosition.x /= parentScale.x;
            self.localPosition.y /= parentScale.y;

    def setScale(self, *args):
        if len(args) == 1:
            scale = args[0]
        elif len(args) == 2:
            scale = Vector2(args[0], args[1])
        
        self.localScale = scale
        if self.parent is not None:
            parentScale = self.parent.getScale()

            self.localScale.x /= parentScale.x
            self.localScale.y /= parentScale.y

    def translate(self, x: float, y: float):
        self.localPosition += Vector2(x, y)

    def setLocalScale(self, xScale: float, yScale: float):
        self.localScale = Vector2(xScale, yScale)

    def updatePosition(self):
        self.position = self.localPosition.copy()

        if self.parent is not None:
            self.position *= self.parent.scale
            self.position += self.parent.position

    def updateScale(self):
        self.scale = self.localScale.copy()
        parent = self.parent

        while parent is not None:
            self.scale *= parent.localScale
            parent = parent.parent

    def updateFlip(self):
        self.flip = self.localFlip.copy()
        parent = self.parent

        while parent is not None:
            parent_flip = parent.localFlip
            if parent_flip.x:
                self.flip.x = not self.flip.x
            if parent_flip.y:
                self.flip.y = not self.flip.y
            parent = parent.parent