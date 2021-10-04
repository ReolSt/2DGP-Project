import pico2d

from .Singleton import *

class RenderingContext(metaclass=Singleton):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        pico2d.open_canvas()
        pico2d.resize_canvas(self.width, self.height)