from Engine.Vector2 import Vector2
from Engine.GameObject import GameObject
from Engine.AudioMixer import AudioMixer

class Level(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.unitSize = Vector2(16, 16)

        self.state = "Playing"

        self.player = None
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

        if self.state == "Playing":
            if self.player.died:
                self.state = "Ending"
                AudioMixer().stopMusic("Overworld")