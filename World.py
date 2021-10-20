from Engine.Vector2 import *
from Engine.AudioMixer import *

from Sky import *
from Ground import *
from Mountain import *
from VerticalPipe import *
from HorizontalPipe import *
from Cloud import *
from Grass import *
from Tree import *
from Mushroom import *
from Flagpole import *

class World(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.unitSize = Vector2(16, 16)
        self.player = None

        self.world = 0
        self.stage = 0

        self.playerInitialPosition = Vector2(0, 0)

        AudioMixer().playMusic("Overworld")

    def gridPosition(self, x, y):
        return Vector2(x * self.unitSize.x, y * self.unitSize.y)

    def setGridPosition(self, gameObject, x, y):
        gameObject.transform.localPosition = self.gridPosition(x, y)

    def setPlayerInitialPosition(self, player):
        playerGridPosition = self.gridPosition(
                                         self.playerInitialPosition.x,
                                         self.playerInitialPosition.y)
        player.transform.localPosition = playerGridPosition

    def addPlayer(self, player):
        self.player = player

    def removePlayer(self):
        self.player = None

    def update(self, deltaTime):
        super().update(deltaTime)

        if self.player is not None:
            if self.player.transform.position.y < 0:
                AudioMixer().stopMusic("Overworld")
                AudioMixer().playWav("MarioDie")
                self.removePlayer()