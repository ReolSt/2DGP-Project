from Engine.GameObject import GameObject
from UILoader import UILoader

class GameOverUI(GameObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.layer = "UI"

        self.slots = UILoader().load(self, "GameOver")

        for slot in self.slots.values():
            self.addChild(slot.gameObject)
            slot.gameObject.layer = "UI"

        self.slots["WorldText"].gameObject.setText("WORLD")
        self.slots["TimeText"].gameObject.setText("TIME")
        self.slots["GameOverText"].gameObject.setText("GAME OVER")

    def update(self, deltaTime):
        super().update(deltaTime)

        self.slots["Name"].gameObject.setText(self.name)
        self.slots["Score"].gameObject.setText(str(self.score).zfill(6))
        self.slots["Coin"].gameObject.setText("*" + str(self.coin).zfill(2))
        self.slots["WorldStage"].gameObject.setText(str(self.world) + "-" + str(self.stage))