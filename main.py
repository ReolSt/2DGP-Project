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
from Engine.Camera import *
from Engine.Scene import *

from GameState import *
from GamePlayInterface import *

from PlayerController import *
from World1_1 import *

scene = Scene("SuperMarioBros")

root = scene.root

ui = GameObject(root)
world = World1_1(root)

root.children.append(ui)
root.children.append(world)

worldCamera = scene.addCamera(parent=root, layer="Default", order=2)
backgroundCamera = scene.addCamera(parent=root, layer="Background", order=1)

world.children.append(worldCamera)
world.children.append(backgroundCamera)

uiCamera = scene.addCamera(parent=ui, layer="UI", order=3)
ui.children.append(uiCamera)

playerController = PlayerController(world)
playerController.player.transform.translate(100, 116)
playerController.player.transform.setScale(3.0, 3.0)

world.children.append(playerController)

gameState = GameState(root)
root.children.append(gameState)

gamePlayInterface = GamePlayInterface(ui, gameState)
ui.children.append(gamePlayInterface)

running = True
oldTime = time.time()
while running:
    currentTime = time.time()
    deltaTime = currentTime - oldTime

    pico2d.clear_canvas()

    scene.update(deltaTime * 1000)
    scene.render()

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