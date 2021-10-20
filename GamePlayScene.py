from Engine.Vector2 import *
from Engine.GameObject import *
from Engine.Text import *
from Engine.Camera import *
from Engine.Scene import *
from Engine.AudioMixer import *

from WorldImporter import *

from GameState import *
from GamePlayInterface import *

from PlayerController import *

class GamePlayScene(Scene):
    def __init__(self, name=""):
        super().__init__(name)

        ui = GameObject(self.root)
        self.root.addChild(ui)

        uiCamera = self.addCamera(parent=ui, layer="UI", order=3)
        ui.addChild(uiCamera)

        gamePlayInterface = GamePlayInterface(ui)
        ui.addChild(gamePlayInterface)


    def loadWorld(self, worldNumber, stageNumber):
        self.world = WorldImporter().importWorld(self.root, worldNumber, stageNumber)

        self.root.addChild(self.world)

        gameState = GameState()
        gameState.time = 400
        gameState.world = self.world.world
        gameState.stage = self.world.stage

        backgroundCamera = self.addCamera(parent=self.root, layer="Background", order=1)
        worldCamera = self.addCamera(parent=self.root, layer="Default", order=2)

        self.world.addChild(worldCamera)
        self.world.addChild(backgroundCamera)

        playerController = PlayerController(self.world, worldCamera)
        playerController.player.transform.setScale(1.5, 1.5)

        self.world.setPlayerInitialPosition(playerController.player)

        self.world.addChild(playerController)
        self.world.addPlayer(playerController.player)

        self.world.transform.setScale(2, 2)