import math

from .Vector2 import *

class Transform:
    def __init__(self, parent=None, gameObject=None):
        assert isinstance(parent, Transform) or parent is None, "Invalid parameter type: {}".format(parent)

        self.parent = parent
        self.gameObject = gameObject

        self.localPosition = Vector2(0.0, 0.0)
        self.localRotation = 0.0
        self.localScale = Vector2(1.0, 1.0)
        self.localFlip = Vector2(False, False)

        self.position = self.localPosition.copy()
        self.rotation = self.localRotation
        self.scale = self.localScale
        self.flip = self.localFlip

        self.update()

    def update(self):
        self.updateFlip()
        self.updateScale()
        self.updateRotation()
        self.updatePosition()

    def translate(self, x, y):
        self.localPosition += Vector2(x, y)

    def rotate(self, deg):
        self.localRotation += deg

    def setScale(self, xScale, yScale):
        self.localScale = Vector2(xScale, yScale)

    def updatePosition(self):
        self.position = self.localPosition.copy()

        if self.parent is not None:
            self.position *= self.parent.scale

            cos = math.cos(math.radians(self.parent.rotation))
            sin = math.sin(math.radians(self.parent.rotation))

            self.position = Vector2(self.position.x * cos - self.position.y * sin,
                               self.position.y * cos + self.position.x * sin)

            self.position += self.parent.position

    def updateRotation(self):
        self.rotation = self.localRotation
        parent = self.parent

        while parent is not None:
            self.rotation += parent.localRotation
            parent = parent.parent

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