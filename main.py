import time
import numpy

import pico2d

from Engine.Settings import *
from Engine.RenderingContext import *

settings = Settings()
renderingContext = RenderingContext(
    int(settings.default["WindowWidth"]), int(settings.default["WindowHeight"]))

from Engine.GameObject import *
from Engine.Text import *
from Engine.Scene import *

from GameState import *
from GamePlayInterface import *

from Player import *

from Sky import *
from Ground import *
from Mountain import *
from VerticalPipe import *
from Cloud import *
from Grass import *
from Tree import *
from Mushroom import *
from Flagpole import *

scene = Scene("SuperMarioBros")
root = scene.root

backgroundLayer = GameObject(scene.root)
terrainLayer = GameObject(scene.root)
entityLayer = GameObject(scene.root)
interfaceLayer = GameObject(scene.root)

root.children = [backgroundLayer, terrainLayer, entityLayer, interfaceLayer]

sky = Sky(terrainLayer, 800, 600)
sky.transform.translate(0, 0)
backgroundLayer.children.append(sky)

player = Player(entityLayer)
player.transform.translate(100.0, 116.0)
player.transform.setScale(3.0, 3.0)
entityLayer.children.append(player)
scene.collisionManager.addObject(player)

ground = Ground(terrainLayer, 50, 3)
ground.transform.translate(0, 0)
ground.transform.setScale(2, 2)
terrainLayer.children.append(ground)
scene.collisionManager.addObject(ground)

mountain = Mountain(terrainLayer, 3)
mountain.transform.translate(100, 96)
mountain.transform.setScale(2, 2)
terrainLayer.children.append(mountain)

verticalPipe = VerticalPipe(terrainLayer, height=5)
verticalPipe.transform.translate(300, 200)
verticalPipe.transform.setScale(2, 2)
terrainLayer.children.append(verticalPipe)

cloud = Cloud(terrainLayer)
cloud.transform.translate(400, 200)
cloud.transform.setScale(2, 2)
terrainLayer.children.append(cloud)

cloud2 = Cloud(terrainLayer, 4)
cloud2.transform.translate(400, 300)
cloud2.transform.setScale(2, 2)
terrainLayer.children.append(cloud2)

grass = Grass(terrainLayer)
grass.transform.translate(500, 200)
grass.transform.setScale(2, 2)
terrainLayer.children.append(grass)

tree = Tree(terrainLayer)
tree.transform.translate(560, 200)
tree.transform.setScale(2, 2)
terrainLayer.children.append(tree)

mushroom = Mushroom(terrainLayer)
mushroom.transform.translate(640, 200)
mushroom.transform.setScale(2, 2)
terrainLayer.children.append(mushroom)

flagpole = Flagpole(terrainLayer)
flagpole.transform.translate(700, 100)
flagpole.transform.setScale(2, 2)
terrainLayer.children.append(flagpole)

gameState = GameState(root)
gamePlayInterface = GamePlayInterface(interfaceLayer, gameState)

root.children.append(gameState)
interfaceLayer.children.append(gamePlayInterface)


running = True
oldTime = time.time()
while running:
    currentTime = time.time()
    deltaTime = currentTime - oldTime

    pico2d.clear_canvas()

    scene.update(deltaTime * 1000)
    scene.root.render()

    pico2d.update_canvas()

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            running = False
            break
        else:
            scene.root.captureEvent(event)

    finishedTime = time.time()
    elapsedTime = finishedTime - currentTime

    pico2d.delay(max(0.0, 1 / int(settings.default['TargetFPS']) - elapsedTime))

    oldTime = currentTime

pico2d.close_canvas()