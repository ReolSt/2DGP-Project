from Engine.GameObject import *
from Engine.Text import *
from Engine.Camera import *
from Engine.Scene import *

from GameState import *
from GamePlayInterface import *

from PlayerController import *
from World1_1 import *

class World1_1Scene(Scene):
    def __init__(self, name=""):
        super().__init__(name)
        ui = GameObject(self.root)
        world = World1_1(self.root)

        self.root.children.append(ui)
        self.root.children.append(world)

        backgroundCamera = self.addCamera(parent=self.root, layer="Background", order=1)
        worldCamera = self.addCamera(parent=self.root, layer="Default", order=2)

        world.children.append(worldCamera)
        world.children.append(backgroundCamera)

        uiCamera = self.addCamera(parent=ui, layer="UI", order=3)
        ui.children.append(uiCamera)

        playerController = PlayerController(world)
        playerController.player.transform.translate(100, 116)
        playerController.player.transform.setScale(2, 2)

        world.children.append(playerController)

        gameState = GameState(self.root)
        self.root.children.append(gameState)

        gamePlayInterface = GamePlayInterface(ui, gameState)
        ui.children.append(gamePlayInterface)