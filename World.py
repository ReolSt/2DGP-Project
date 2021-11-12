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

        self.ui = GameObject(self)
        self.addChild(self.ui)

        self.uiCamera = self.scene.addCamera(parent=self.ui, layer="UI", order=3)
        self.ui.addChild(self.uiCamera)

        self.gamePlayUI = GamePlayUI(self.ui)
        self.ui.addChild(self.gamePlayUI)

        self.score = 0
        self.coin = 0
        self.world = 0
        self.stage = 0
        self.time = 400

    def update(self, deltaTime):
        super().update(deltaTime)

        self.gamePlayUI.name = self.name
        self.gamePlayUI.score = self.score
        self.gamePlayUI.coin = self.coin
        self.gamePlayUI.world = self.world
        self.gamePlayUI.stage = self.stage
        self.gamePlayUI.time = int(self.time)

        self.time -= deltaTime / 1000

    def loadLevel(self, world, stage, subStage=-1):
        if subStage == -1:
            self.level = LevelLoader().load(self, "{}-{}".format(world, stage))
        else:
            self.level = LevelLoader().load(self, "{}-{}-{}".format(world, stage, subStage))

        self.addChild(self.level)

        self.name = "MARIO"
        self.score = 0
        self.coin = 0
        self.world = world
        self.stage = stage
        self.subStage = subStage
        self.time = 400

        self.backgroundCamera = self.scene.addCamera(parent=self, layer="Background", order=1)
        self.worldCamera = self.scene.addCamera(parent=self, layer="Default", order=2)

        self.level.addChild(self.worldCamera)
        self.level.addChild(self.backgroundCamera)

        self.playerController = PlayerController(self.level, self.worldCamera)
        self.playerController.player.transform.setLocalScale(1.0, 1.0)

        self.level.addChild(self.playerController)
        self.level.addPlayer(self.playerController.player)

        self.level.setPlayerInitialPosition(self.playerController.player)

        self.level.transform.setScale(2.5, 2.5)
