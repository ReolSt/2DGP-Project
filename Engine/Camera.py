import os

if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Settings import Settings
    from Transform import Transform
    from GameObject import GameObject
    from Vector2 import Vector2
else:
    from .Settings import Settings
    from .Transform import Transform
    from .GameObject import GameObject
    from .Vector2 import Vector2

import math
from typing import Union

class Camera(GameObject):
    def __init__(self, parent : GameObject, layer: str ="Default", order : int = 1):
        super().__init__(parent)

        self.layer = layer
        self.order = order

    def translate(self, position: Vector2):
        assert isinstance(position, Vector2), "Invalid parameter type: {}".format(type(position))

        position -= self.transform.position

        return position

    def scale(self, scale: Vector2):
        assert isinstance(scale, Vector2), "Invalid parameter type: {}".format(type(scale))

        return scale * self.transform.scale