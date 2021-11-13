from Engine.GameObject import GameObject
from Engine.Text import Text
from Engine.Camera import Camera
from Engine.Scene import Scene

from LevelLoader import LevelLoader
from GamePlayUI import GamePlayUI
from PlayerController import PlayerController

class World(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

    def load(self, world, stage, subStage=-1):
        if subStage == -1:
            self.level = LevelLoader().load(self, "{}-{}".format(world, stage))
        else:
            self.level = LevelLoader().load(self, "{}-{}-{}".format(world, stage, subStage))

        self.addChild(self.level)

        self.backgroundCamera = self.scene.addCamera(parent=self, layer="Background", order=1)
        self.worldCamera = self.scene.addCamera(parent=self, layer="Default", order=2)

        self.level.addChild(self.worldCamera)
        self.level.addChild(self.backgroundCamera)

        self.playerController = PlayerController(self.level, self.worldCamera)
        self.player = self.playerController.player
        self.player.transform.setLocalScale(1.0, 1.0)

        self.level.addChild(self.playerController)
        self.level.addPlayer(self.playerController.player)

        self.level.setPlayerInitialPosition(self.playerController.player)

        self.level.transform.setScale(2.5, 2.5)
