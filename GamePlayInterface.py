from Engine.GameObject import *
from Engine.Text import *
from Engine.EntitySprite import *

from GameState import *


class GamePlayInterface(GameObject):
    def __init__(self, parent):
        super().__init__(parent)
        gameState = GameState()

        self.layer = "UI"

        self.name = Text(self, gameState.name, 1)
        self.name.transform.translate(80, 568)
        self.name.transform.setLocalScale(3, 3)
        self.name.layer = "UI"

        self.score = Text(self, str(gameState.score).zfill(6), 1)
        self.score.transform.translate(80, 544)
        self.score.transform.setLocalScale(3, 3)
        self.score.layer = "UI"

        self.coin = GameObject(self)
        self.coin.sprites.append(EntitySprite(self.coin, "Coin3"))
        self.coin.transform.translate(272, 544)
        self.coin.transform.setLocalScale(2, 2)
        self.coin.layer = "UI"

        self.coinCount = Text(self, "*" + str(gameState.coin).zfill(2), 1)
        self.coinCount.transform.translate(298, 544)
        self.coinCount.transform.setLocalScale(3, 3)
        self.coinCount.layer = "UI"

        self.world = Text(self, "WORLD", 1)
        self.world.transform.translate(464, 568)
        self.world.transform.setLocalScale(3, 3)
        self.world.layer = "UI"

        self.worldStage = Text(self, str(gameState.world) + "-" + str(gameState.stage), 1)
        self.worldStage.transform.translate(488, 544)
        self.worldStage.transform.setLocalScale(3, 3)
        self.worldStage.layer = "UI"

        self.time = Text(self, "TIME", 1)
        self.time.transform.translate(640, 568)
        self.time.transform.setLocalScale(3, 3)
        self.time.layer = "UI"

        self.timeCount = Text(self, str(gameState.time).zfill(3), 1)
        self.timeCount.transform.translate(656, 544)
        self.timeCount.transform.setLocalScale(3, 3)
        self.timeCount.layer = "UI"

        self.addChildren([
            self.name, self.score,
            self.coin, self.coinCount,
            self.world, self.worldStage,
            self.time, self.timeCount])

    def update(self, deltaTime):
        super().update(deltaTime)
        gameState = GameState()

        self.name.setText(gameState.name)
        self.score.setText(str(gameState.score).zfill(6))
        self.coinCount.setText("*" + str(gameState.coin).zfill(2))
        self.worldStage.setText(str(gameState.world) + "-" + str(gameState.stage))
        self.timeCount.setText(str(int(gameState.time)).zfill(3))