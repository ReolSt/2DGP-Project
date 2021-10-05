import pico2d
from .GameObject import *
from .CollisionManager import *

class Scene:
    def __init__(self, name=""):
        self.name = name
        self.root = GameObject(None)
        self.collisionManager = CollisionManager(self)

    def update(self, deltaTime):
        self.root.update(deltaTime)
        self.collisionManager.Update()