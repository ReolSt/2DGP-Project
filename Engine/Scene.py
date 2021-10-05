import pico2d
from .GameObject import *
from .CollisionManager import *

class Scene:
    def __init__(self, name=""):
        self.name = name
        self.root = GameObject(None)
        self.collisionManager = CollisionManager(self)

    def Update(self, deltaTime):
        self.root.Update(deltaTime)
        self.collisionManager.Update()