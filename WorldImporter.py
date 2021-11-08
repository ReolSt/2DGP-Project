from Engine.Singleton import *
from Engine.Settings import *
from Engine.Scene import *

from World import *

from Sky import *
from Ground import *
from Mountain import *
from Block import *
from MysteryBlock import *
from Brick import *
from VerticalPipe import *
from HorizontalPipe import *
from Cloud import *
from Grass import *
from Tree import *
from Mushroom import *
from Flagpole import *

class WorldImporter(metaclass=Singleton):
    def __init__(self):
        self.worldFilePath = Settings().world["WorldFilePath"]

    def importWorld(self, parent, worldNumber, stageNumber):
        filePath = self.worldFilePath + "{}-{}.txt".format(worldNumber, stageNumber)

        world = World(parent)
        world.world = worldNumber
        world.stage = stageNumber

        parserState = "Player"

        with open(filePath, "r") as file:
            i = 0
            for line in file.readlines():
                tokens = line.split()

                if parserState == "Player":
                    assert len(tokens) == 2
                    x, y = map(int, tokens)
                    world.playerInitialPosition.x = x
                    world.playerInitialPosition.y = y

                    parserState = "Background"
                    continue
                elif parserState == "Background":
                    assert len(tokens) == 1
                    objectName = str(tokens[0])

                    gameObject = None
                    if objectName == "Sky":
                        gameObject = Sky(world, 800, 600)

                    if gameObject is not None:
                        gameObject.layer = "Background"
                        world.addChild(gameObject)

                    parserState = "GameObject"
                    continue

                if len(tokens) == 0:
                    continue

                assert 5 <= len(tokens) <= 6

                objectName, x, y, width, height = tokens[:5]
                x, y, width, height = int(x), int(y), int(width), int(height)

                if len(tokens) == 6:
                    colorType = int(tokens[5])

                gameObject = None

                if objectName == "Ground":
                    gameObject = Ground(world, width, height)
                elif objectName == "Mountain":
                    gameObject = Mountain(world, height)
                elif objectName == "Block":
                    gameObject = Block(world, width, height)
                elif objectName == "MysteryBlock":
                    gameObject = MysteryBlock(world, colorType)
                elif objectName == "Brick":
                    gameObject = Brick(world, width, height)
                elif objectName == "VerticalPipe":
                    gameObject = VerticalPipe(world, height)
                elif objectName == "HorizontalPipe":
                    gameObject = HorizontalPipe(world, width, height)
                elif objectName == "Cloud":
                    gameObject = Cloud(world, width)
                elif objectName == "Grass":
                    gameObject = Grass(world, width)
                elif objectName == "Tree":
                    gameObject = Tree(world, height)
                elif objectName == "Mushroom":
                    gameObject = Mushroom(world, width, height)
                elif objectName == "Flagpole":
                    gameObject = Flagpole(world, height)

                if gameObject is not None:
                    world.setGridPosition(gameObject, x, y)
                    world.addChild(gameObject)

        return world