from .Settings import *
from .Transform import *
from .GameObject import *

class Camera(GameObject):
    def __init__(self, parent, layer="Default", order=1):
        super().__init__(parent)

        self.layer = layer
        self.order = order

    def translate(self, position):
        assert isinstance(position, Vector2), "Invalid parameter type: {}".format(type(position))

        position = position.copy()

        cameraPosition = -self.transform.position()
        cameraRotation = -self.transform.rotation()
        cameraScale = self.transform.scale()

        cos = numpy.cos(numpy.deg2rad(cameraRotation))
        sin = numpy.sin(numpy.deg2rad(cameraRotation))

        position *= cameraScale
        position = Vector2(position.x * cos - position.y * sin,
                           position.y * cos + position.x * sin)
        position += cameraPosition

        return position

    def rotate(self, rotation):
        assert isinstance(rotation, int) or isinstance(rotation, float), "Invalid parameter type: {}".format(type(rotation))
        return rotation - self.transform.rotation()

    def scale(self, scale):
        assert isinstance(scale, Vector2), "Invalid parameter type: {}".format(type(scale))

        return scale * self.transform.scale()