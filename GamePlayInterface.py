from Engine.GameObject import *
from Engine.TextObject import *
from Engine.EntityObject import *
from GameState import *


class GamePlayInterface(GameObject):
    def __init__(self, parent, gameState):
        super().__init__(parent)
        self.gameState = gameState

        self.name = TextObject(self, gameState.name, 1)
        self.name.transform.translate(80, 568)
        self.name.transform.setScale(3, 3)
        self.children.append(self.name)

        self.score = TextObject(self, str(gameState.score).zfill(6), 1)
        self.score.transform.translate(80, 544)
        self.score.transform.setScale(3, 3)
        self.children.append(self.score)

        self.coin = EntityObject(self, "Coin3")
        self.coin.transform.translate(272, 544)
        self.coin.transform.setScale(2, 2)
        self.children.append(self.coin)

        self.coinCount = TextObject(self, "*" + str(gameState.coin).zfill(2), 1)
        self.coinCount.transform.translate(298, 544)
        self.coinCount.transform.setScale(3, 3)
        self.children.append(self.coinCount)

        self.world = TextObject(self, "WORLD", 1)
        self.world.transform.translate(464, 568)
        self.world.transform.setScale(3, 3)
        self.children.append(self.world)

        self.worldStage = TextObject(self, str(gameState.world) + "-" + str(gameState.stage), 1)
        self.worldStage.transform.translate(488, 544)
        self.worldStage.transform.setScale(3, 3)
        self.children.append(self.worldStage)

        self.time = TextObject(self, "TIME", 1)
        self.time.transform.translate(640, 568)
        self.time.transform.setScale(3, 3)
        self.children.append(self.time)

        self.timeCount = TextObject(self, str(gameState.time).zfill(3), 1)
        self.timeCount.transform.translate(656, 544)
        self.timeCount.transform.setScale(3, 3)
        self.children.append(self.timeCount)

    def update(self, deltaTime):
        super().update(deltaTime)

        self.name.setText(self.gameState.name)
        self.score.setText(str(self.gameState.score).zfill(6))
        self.coinCount.setText(str(self.gameState.coin).zfill(2))
        self.worldStage.setText(str(self.gameState.world) + "-" + str(self.gameState.stage))
        self.timeCount.setText(str(self.gameState.time).zfill(3))