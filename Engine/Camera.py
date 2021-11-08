import os

if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Settings import *
    from Transform import *
    from GameObject import *
else:
    from .Settings import *
    from .Transform import *
    from .GameObject import *

import math
from typing import Union

class Camera(GameObject):
    def __init__(self, parent : GameObject, layer: str ="Default", order : int = 1):
        super().__init__(parent)

        self.layer = layer
        self.order = order

    def translate(self, position: Vector2):
        assert isinstance(position, Vector2), "Invalid parameter type: {}".format(type(position))

        cos = self.transform.rotationCos
        sin = -self.transform.rotationSin

        position = position * self.transform.scale
        position = Vector2(position.x * cos - position.y * sin,
                           position.y * cos + position.x * sin)
        position -= self.transform.position

        return position

    def rotate(self, rotation: float):
        assert isinstance(rotation, int) or isinstance(rotation, float), "Invalid parameter type: {}".format(type(rotation))
        return rotation - self.transform.rotation

    def scale(self, scale: Vector2):
        assert isinstance(scale, Vector2), "Invalid parameter type: {}".format(type(scale))

        return scale * self.transform.scale