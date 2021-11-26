import pico2d

from Engine.GameObject import GameObject
from Engine.AudioMixer import AudioMixer

from World import World
from MainMenuUI import MainMenuUI
from PreGameUI import PreGameUI
from GamePlayUI import GamePlayUI
from GameOverUI import GameOverUI
from Objects.Background import Background

from enum import Enum

class MainMenu(GameObject):
    def __init__(self, game):
        super().__init__(game)

        self.game = game
        self.game.hardReset()

        self.ui = MainMenuUI(self.game)
        self.ui.name = self.game.name
        self.ui.life  = self.game.life
        self.ui.score = self.game.score
        self.ui.coin = self.game.coin
        self.ui.world = self.game.worldNumber
        self.ui.stage = self.game.stageNumber

        self.game.world = World(self)
        self.game.world.load(1, 0, -1)
        self.game.world.playerController.input = False

        self.game.addChildren([self.ui, self.game.world])

        self.uiCamera = self.game.scene.addCamera(parent=self.game, layer="UI", order=3)
        self.game.addChild(self.uiCamera)

    def onKeyDown(self, event):
        if event.key == pico2d.SDLK_RETURN:
            self.game.state = PreGame(self.game)

class PreGame(GameObject):
    def __init__(self, game):
        super().__init__(game)

        self.game = game
        self.game.softReset()

        self.background = Background(self.game, 800, 600, "Black")
        self.background.layer = "UI"
        self.game.addChild(self.background)

        self.ui = PreGameUI(self.game)
        self.ui.name = self.game.name
        self.ui.life  = self.game.life
        self.ui.score = self.game.score
        self.ui.coin = self.game.coin
        self.ui.world = self.game.worldNumber
        self.ui.stage = self.game.stageNumber

        self.game.addChild(self.ui)

        self.uiCamera = self.game.scene.addCamera(parent=self.game, layer="UI", order=3)
        self.game.addChild(self.uiCamera)

    def onKeyDown(self, event):
        if event.key == pico2d.SDLK_RETURN:
            self.game.state = GamePlay(self.game)

class GamePlay(GameObject):
    def __init__(self, game):
        super().__init__(game)

        self.game = game
        self.game.softReset()

        self.ui = GamePlayUI(self.game)

        self.game.world = World(self)
        self.game.world.load(self.game.worldNumber, self.game.stageNumber, self.game.subStage)

        self.game.addChildren([self.ui, self.game.world])

        self.uiCamera = self.game.scene.addCamera(parent=self.game, layer="UI", order=3)
        self.game.addChild(self.uiCamera)

        self.game.world.level.playBGM()

    def onKeyDown(self, event):
        if self.game.world.player.died and event.key == pico2d.SDLK_RETURN:
            self.game.life -= 1
            if self.game.life > 0:
                self.game.state = PreGame(self.game)
            else:
                self.game.state = GameOver(self.game)

        self.ui.name = self.game.name
        self.ui.life = self.game.life
        self.ui.score = self.game.score
        self.ui.coin = self.game.coin
        self.ui.world = self.game.worldNumber
        self.ui.stage = self.game.stageNumber
        self.ui.time = int(self.game.time)

        self.game.time -= deltaTime / 1000

class GameOver(GameObject):
    def __init__(self, game):
        super().__init__(game)

        self.game = game
        self.game.softReset()

        self.background = Background(self.game, 800, 600, "Black")
        self.background.layer = "UI"
        self.game.addChild(self.background)

        self.ui = GameOverUI(self.game)
        self.ui.name = self.game.name
        self.ui.life  = self.game.life
        self.ui.score = self.game.score
        self.ui.coin = self.game.coin
        self.ui.world = self.game.worldNumber
        self.ui.stage = self.game.stageNumber

        self.game.addChild(self.ui)

        self.uiCamera = self.game.scene.addCamera(parent=self.game, layer="UI", order=3)
        self.game.addChild(self.uiCamera)

        AudioMixer().playWav("GameOver")

    def onKeyDown(self, event):
        super().onKeyDown(event)

        if event.key == pico2d.SDLK_RETURN or event.key == pico2d.SDLK_ESCAPE:
            self.game.state = MainMenu(self.game)

class Game(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.hardReset()
        self.state = MainMenu(self)

    def softReset(self):
        self.clearChildren()
        self.scene.clearCamera()
        self.scene.physicsManager.reset()

    def hardReset(self):
        self.softReset()

        self.name = "MARIO"
        self.life = 3
        self.score = 0
        self.coin = 0
        self.worldNumber = 1
        self.stageNumber = 1
        self.subStage = -1
        self.time = 400
        self.world = None

    def onKeyDown(self, event):
        super().onKeyDown(event)

        self.state.onKeyDown(event)

    def update(self, deltaTime):
        super().update(deltaTime)

        self.state.update(deltaTime)