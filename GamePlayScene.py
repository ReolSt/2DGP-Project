from Engine.Vector2 import *
from Engine.GameObject import *
from Engine.Text import *
from Engine.Camera import *
from Engine.Scene import *
from Engine.AudioMixer import *

from GameState import *
from GamePlayInterface import *

from PlayerController import *

class GamePlayScene(Scene):
    def __init__(self, worldClassType, name=""):
        super().__init__(name)
        ui = GameObject(self.root)
        world = worldClassType(self.root, Vector2(16, 16))

        self.root.children.append(ui)
        self.root.children.append(world)

        backgroundCamera = self.addCamera(parent=self.root, layer="Background", order=1)
        worldCamera = self.addCamera(parent=self.root, layer="Default", order=2)

        world.children.append(worldCamera)
        world.children.append(backgroundCamera)

        playerController = PlayerController(world, worldCamera)
        playerController.player.transform.translate(100, 116)
        playerController.player.transform.setScale(1.5, 1.5)

        uiCamera = self.addCamera(parent=ui, layer="UI", order=3)
        ui.children.append(uiCamera)

        world.children.append(playerController)
        world.addPlayer(playerController.player)

        world.transform.setScale(2, 2)

        gameState = GameState(self.root)
        self.root.children.append(gameState)

        gamePlayInterface = GamePlayInterface(ui, gameState)
        ui.children.append(gamePlayInterface)