import pico2d
import os

if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Singleton import *
else:
    from .Singleton import *

class RenderingContext(metaclass=Singleton):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        pico2d.open_canvas()
        pico2d.resize_canvas(self.width, self.height)