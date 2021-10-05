import time
import numpy

import pico2d

from Engine.Settings import *
from Engine.RenderingContext import *

settings = Settings()
renderingContext = RenderingContext(
    int(settings.default["WindowWidth"]), int(settings.default["WindowHeight"]))

from Engine.GameObject import *
from Engine.TextObject import *
from Engine.BackgroundObject import *
from Engine.TerrainObject import *
from Engine.Scene import *

from GamePlayInterface import *
from Player import *
from Mountain import *
from VerticalPipe import *
from Cloud import *
from Grass import *

scene = Scene("SuperMarioBros")
root = scene.root

backgroundLayer = GameObject(scene.root)
terrainLayer = GameObject(scene.root)
entityLayer = GameObject(scene.root)
interfaceLayer = GameObject(scene.root)

root.children = [backgroundLayer, terrainLayer, entityLayer, interfaceLayer]

sky = BackgroundObject(backgroundLayer, "Sky")
sky.transform.translate(400.0, 300.0)
backgroundLayer.children.append(sky)

player = Player(entityLayer)
player.transform.translate(100.0, 100.0)
player.transform.setScale(3.0, 3.0)
entityLayer.children.append(player)

block = TerrainObject(terrainLayer, "Ground")
block.transform.translate(100.0, 50.0)
block.transform.setScale(2, 2)
terrainLayer.children.append(block)

mountain = Mountain(terrainLayer)
mountain.transform.translate(200, 200)
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

grass = Grass(terrainLayer)
grass.transform.translate(500, 200)
grass.transform.setScale(2, 2)
terrainLayer.children.append(grass)

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