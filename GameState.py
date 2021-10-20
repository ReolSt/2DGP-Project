from Engine.Singleton import *
from Engine.GameObject import *

class GameState(metaclass=Singleton):
    def __init__(self):
        self.name = "MARIO"
        self.score = 0
        self.coin = 0
        self.world = 1
        self.stage = 1
        self.time = 0

    def update(self, deltaTime):
        self.time -= deltaTime / 1000