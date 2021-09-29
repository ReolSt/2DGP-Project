import pico2d
from GameObject import *

class Scene:
    def __init__(self, name=""):
        self.name = name
        self.root = GameObject(None)