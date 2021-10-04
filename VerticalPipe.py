from Engine.TerrainSprite import *
from Engine.GameObject import *

class VerticalPipe(GameObject):
    def __init__(self, parent, height=2):
        super().__init__(parent)

        assert(height > 0)

        height_offset = 0

        for h in range(height - 1):
            pillarLeft = TerrainSprite(self.transform, "VerticalPipePillar1")
            pillarRight = TerrainSprite(self.transform, "VerticalPipePillar2")

            pillarLeft.transform.translate(-pillarLeft.width / 2, height_offset)
            pillarRight.transform.translate(pillarRight.width / 2, height_offset)

            height_offset += pillarLeft.height

            self.sprites.append(pillarLeft)
            self.sprites.append(pillarRight)

        entranceLeft = TerrainSprite(self.transform, "VerticalPipeEntrance1")
        entranceRight = TerrainSprite(self.transform, "VerticalPipeEntrance2")

        entranceLeft.transform.translate(-entranceLeft.width / 2, height_offset)
        entranceRight.transform.translate(entranceRight.width / 2, height_offset)

        self.sprites.append(entranceLeft)
        self.sprites.append(entranceRight)