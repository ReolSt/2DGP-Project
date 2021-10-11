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

class World1_1(GameObject):
    def __init__(self, parent):
        super().__init__(parent)
        sky = Sky(self, 800, 600)
        sky.layer = "Background"

        self.children.append(sky)

        ground = Ground(self, 50, 3)
        ground.transform.translate(0, 0)
        ground.transform.setScale(2, 2)
        self.children.append(ground)

        mountain = Mountain(self, 3)
        mountain.transform.translate(100, 96)
        mountain.transform.setScale(2, 2)
        self.children.append(mountain)

        verticalPipe = VerticalPipe(self, height=3)
        verticalPipe.transform.translate(300, 100)
        verticalPipe.transform.setScale(2, 2)
        self.children.append(verticalPipe)

        horizontalPipe = HorizontalPipe(self)
        horizontalPipe.transform.translate(400, 100)
        horizontalPipe.transform.setScale(2, 2)
        self.children.append(horizontalPipe)

        cloud = Cloud(self)
        cloud.transform.translate(400, 200)
        cloud.transform.setScale(2, 2)
        self.children.append(cloud)

        cloud2 = Cloud(self, 4)
        cloud2.transform.translate(400, 300)
        cloud2.transform.setScale(2, 2)
        self.children.append(cloud2)

        grass = Grass(self)
        grass.transform.translate(500, 200)
        grass.transform.setScale(2, 2)
        self.children.append(grass)

        tree = Tree(self)
        tree.transform.translate(560, 200)
        tree.transform.setScale(2, 2)
        self.children.append(tree)

        mushroom = Mushroom(self)
        mushroom.transform.translate(640, 200)
        mushroom.transform.setScale(2, 2)
        self.children.append(mushroom)

        flagpole = Flagpole(self)
        flagpole.transform.translate(700, 100)
        flagpole.transform.setScale(2, 2)
        self.children.append(flagpole)