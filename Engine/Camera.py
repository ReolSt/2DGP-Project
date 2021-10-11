from .Settings import *
from .Transform import *
from .GameObject import *

class Camera(GameObject):
    def __init__(self, parent, layer="Default", order=1):
        super().__init__(parent)

        self.layer = layer
        self.order = order