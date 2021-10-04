from Engine.GameObject import *

class GameState(GameObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "MARIO"
        self.score = 0
        self.coin = 0
        self.world = 1
        self.stage = 1
        self.time = 0
