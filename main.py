import time
import numpy

import pico2d

from Settings import *
from RenderingContext import *

settings = Settings()
renderingContext = RenderingContext(
    int(settings.default["WindowWidth"]), int(settings.default["WindowHeight"]))

from Sprite import *
from SpriteMap import *
from SpriteIndexParser import *
from GameObject import *
from TextObject import *
from EntityObject import *
from TerrainObject import *
from BackgroundObject import *
from Scene import *

from GamePlayInterface import *
from Player import *

scene = Scene("SuperMarioBros")
root = scene.root

backgroundLayer = GameObject(scene.root)
objectLayer = GameObject(scene.root)
entityLayer = GameObject(scene.root)
interfaceLayer = GameObject(scene.root)

root.children = [backgroundLayer, objectLayer, entityLayer, interfaceLayer]

sky = BackgroundObject(backgroundLayer, "Sky")
sky.transform.localPosition = numpy.array([400.0, 300.0])
backgroundLayer.children.append(sky)

player = Player(entityLayer)
player.transform.localPosition = numpy.array([100.0, 100.0])
player.transform.localScale = numpy.array([3.0, 3.0])
entityLayer.children.append(player)

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

    scene.root.update(deltaTime * 1000)
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