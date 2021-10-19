from Engine.Vector2 import *

from Sky import *
from Ground import *
from Mountain import *
from VerticalPipe import *
from HorizontalPipe import *
from Cloud import *
from Grass import *
from Tree import *
from Mushroom import *
from Flagpole import *

class World(GameObject):
    def __init__(self, parent, unitSize = Vector2(16, 16)):
        super().__init__(parent)

        self.unitSize = unitSize

    def setGridPosition(self, gameObject, x, y):
        gameObject.transform.localPosition = Vector2(
            x * self.unitSize.x, y * self.unitSize.y)

class World1_1(World):
    def __init__(self, parent):
        super().__init__(parent)
        sky = Sky(self, 800, 600)
        sky.layer = "Background"

        self.children.append(sky)

        ground = Ground(self, 50, 3)
        self.children.append(ground)

        mountain = Mountain(self, 3)
        self.setGridPosition(mountain, 10, 3)
        self.children.append(mountain)

        verticalPipe = VerticalPipe(self, height=3)
        self.setGridPosition(verticalPipe, 15, 3)
        self.children.append(verticalPipe)

        horizontalPipe = HorizontalPipe(self)
        self.setGridPosition(horizontalPipe, 20, 3)
        self.children.append(horizontalPipe)

        cloud = Cloud(self)
        self.setGridPosition(cloud, 15, 20)
        self.children.append(cloud)

        cloud2 = Cloud(self, 4)
        self.setGridPosition(cloud2, 25, 22)
        self.children.append(cloud2)

        grass = Grass(self)
        self.setGridPosition(grass, 25, 3)
        self.children.append(grass)

        tree = Tree(self)
        self.setGridPosition(tree, 30, 3)
        self.children.append(tree)

        mushroom = Mushroom(self)
        self.setGridPosition(mushroom, 35, 3)
        self.children.append(mushroom)

        flagpole = Flagpole(self)
        self.setGridPosition(flagpole, 45, 3)
        self.children.append(flagpole)