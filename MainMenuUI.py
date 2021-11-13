from Engine.GameObject import GameObject
from Engine.GameObject import GameObject
from UILoader import UILoader

class MainMenuUI(GameObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.layer = "UI"

        self.slots = UILoader().load(self, "MainMenu")

        for slot in self.slots.values():
            self.addChild(slot.gameObject)
            slot.gameObject.layer = "UI"

        self.slots["WorldText"].gameObject.setText("WORLD")
        self.slots["TimeText"].gameObject.setText("TIME")
        self.slots["OnePlayerGame"].gameObject.setText("1 PLAYER GAME")
        self.slots["TwoPlayerGame"].gameObject.setText("2 PLAYER GAME")
        self.slots["TopText"].gameObject.setText("TOP-")
        self.slots["TopScore"].gameObject.setText("000000")

    def update(self, deltaTime):
        super().update(deltaTime)

        self.slots["Name"].gameObject.setText(self.name)
        self.slots["Score"].gameObject.setText(str(self.score).zfill(6))
        self.slots["Coin"].gameObject.setText("*" + str(self.coin).zfill(2))
        self.slots["WorldStage"].gameObject.setText(str(self.world) + "-" + str(self.stage))