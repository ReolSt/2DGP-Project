import numpy
from .Vector2 import *

class Transform:
    def __init__(self, parent=None):
        assert(isinstance(parent, Transform) or parent is None)

        self.parent = parent

        self.localPosition = Vector2(0.0, 0.0)
        self.localRotation = 0.0
        self.localScale = Vector2(1.0, 1.0)

        self.localFlip = Vector2(False, False)

    def translate(self, x, y):
        self.localPosition += Vector2(x, y)

    def rotate(self, deg):
        self.localRotation += deg

    def setScale(self, xScale, yScale):
        self.localScale = Vector2(xScale, yScale)

    def position(self):
        parent = self.parent
        position = self.localPosition.copy()
        if parent is not None:
            parent_position = parent.position()
            parent_rotation = parent.rotation()
            parent_scale = parent.scale()

            position *= parent_scale

            cos = numpy.cos(numpy.deg2rad(parent_rotation))
            sin = numpy.sin(numpy.deg2rad(parent_rotation))

            position = Vector2(position.x * cos - position.y * sin,
                               position.y * cos + position.x * sin)

            position += parent_position

        return position

    def rotation(self):
        rotation = self.localRotation
        if self.parent is not None:
            rotation += self.parent.rotation()

        return rotation

    def scale(self):
        scale = self.localScale.copy()
        if self.parent is not None:
            scale *= self.parent.scale()

        return scale

    def flip(self):
        flip = self.localFlip.copy()
        if self.parent is not None:
            parent_flip = self.parent.flip()
            if parent_flip.x:
                flip.x = not flip.x
            if parent_flip.y:
                flip.y = not flip.y

        return flip