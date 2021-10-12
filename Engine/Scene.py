import pico2d
from .GameObject import *
from .CollisionManager import *
from .Camera import *

class Scene:
    def __init__(self, name=""):
        self.name = name
        self.root = GameObject(None)
        self.root.scene = self

        self.collisionManager = CollisionManager(self)
        self.cameras = []

        self.debug = False

    def update(self, deltaTime):
        self.collisionManager.Update()
        self.root.update(deltaTime)

    def render(self):
        for camera in self.cameras:
            self.root.render(camera, self.debug)

    def addCamera(self, parent, layer, order):
        camera = Camera(parent, layer, order)

        self.cameras.append(camera)
        self.cameras.sort(key=lambda camera: camera.order)

        return camera

    def removeCamera(self, camera):
        self.cameras.remove(camera)