from Engine.GameObject import GameObject
from Engine.Text import Text
from Engine.EntitySprite import EntitySprite

from UILoader import UILoader

class GamePlayUI(GameObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.layer = "UI"

        self.slots = UILoader().load(self, "GamePlay")

        for slot in self.slots.values():
            self.addChild(slot.gameObject)
            slot.gameObject.layer = "UI"

        self.slots["WorldText"].gameObject.setText("WORLD")
        self.slots["TimeText"].gameObject.setText("TIME")

        self.name = ""
        self.score = 0
        self.coin = 0
        self.world = 0
        self.stage = 0
        self.time = 0

    def update(self, deltaTime):
        super().update(deltaTime)

        self.slots["Name"].gameObject.setText(self.name)
        self.slots["Score"].gameObject.setText(str(self.score).zfill(6))
        self.slots["Coin"].gameObject.setText("*" + str(self.coin).zfill(2))
        self.slots["WorldStage"].gameObject.setText(str(self.world) + "-" + str(self.stage))
        self.slots["Time"].gameObject.setText(str(int(self.time)).zfill(3))