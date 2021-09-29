import time
import numpy

import pico2d
from Sprite import *
from GameObject import *
from TextObject import *
from Scene import *

TARGET_FPS = 30
WINDOW_SIZE = numpy.array([800, 600])

pico2d.open_canvas()

entitySpriteMap = SpriteMap("Entity")
objectSpriteMap = SpriteMap("Object")
fontSpriteMap = SpriteMap("Font")
backgroundSpriteMap = SpriteMap("Background")

def draw_interface():
    global score, coin, world, time

    drawText("MARIO", 3, 80, 568, (3, 3))
    drawText(str(score).zfill(6), 3, 80, 544, (3, 3))

    draw_sprite(entity_sprite_image, entity_sprite_indices["Coin3"], 272, 544, (2, 2))
    drawText("*" + str(coin).zfill(2), 3, 298, 544, (3, 3))

    drawText("WORLD", 3, 464, 568, (3, 3))
    drawText(str(world) + "-" + str(stage), 6, 488, 544, (3, 3))

    drawText("TIME", 5, 640, 568, (3, 3))
    drawText(str(time).zfill(3), 3, 662, 544, (3, 3))

scene = Scene("SuperMarioBros")
root = scene.root

backgroundLayer = GameObject(scene.root)
objectLayer = GameObject(scene.root)
entityLayer = GameObject(scene.root)
interfaceLayer = GameObject(scene.root)

root.children += [backgroundLayer, objectLayer, entityLayer, interfaceLayer]

backgroundObject = GameObject(backgroundLayer)
backgroundSprite = Sprite(backgroundSpriteMap, "Background", backgroundObject)
backgroundObject.sprites.append(backgroundSprite)
backgroundObject.transform.localPosition = numpy.array([400.0, 300.0])

backgroundLayer.children.append(backgroundObject)

mario = GameObject(scene.root)

class GameState(GameObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.score = 0
        self.coin = 0
        self.world = 1
        self.stage = 1
        self.time = 0

class GUI(GameObject):
    def __init__(self, parent, gameState):
        super().__init__(parent)
        self.gameState = gameState

        marioTextObject = TextObject(self.transform, "MARIO", 3)
        marioTextObject.transform.position

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

    pico2d.delay(max(0.0, 1 / TARGET_FPS - elapsedTime))

pico2d.close_canvas()