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

mario = GameObject(entityLayer)
mario.transform.localPosition = numpy.array([100.0, 100.0])
mario.transform.localScale = numpy.array([3.0, 3.0])
marioSprite = Sprite(entitySpriteMap, "MarioStand", mario)
mario.sprites.append(marioSprite)
entityLayer.children.append(mario)

class GameState(GameObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "MARIO"
        self.score = 0
        self.coin = 0
        self.world = 1
        self.stage = 1
        self.time = 0

class GamePlayInterface(GameObject):
    def __init__(self, parent, gameState):
        super().__init__(parent)
        self.gameState = gameState

        self.name = TextObject(self, fontSpriteMap, gameState.name, 1)
        self.name.transform.translate(80, 568)
        self.name.transform.setScale(3, 3)
        self.children.append(self.name)

        self.score = TextObject(self, fontSpriteMap, str(gameState.score).zfill(6), 1)
        self.score.transform.translate(80, 544)
        self.score.transform.setScale(3, 3)
        self.children.append(self.score)

        self.coin = GameObject(self)
        self.coin.sprites.append(Sprite(entitySpriteMap, "Coin3", self.coin))
        self.coin.transform.translate(272, 544)
        self.coin.transform.setScale(2, 2)
        self.children.append(self.coin)

        self.coinCount = TextObject(self, fontSpriteMap, "*" + str(gameState.coin).zfill(2), 1)
        self.coinCount.transform.translate(298, 544)
        self.coinCount.transform.setScale(3, 3)
        self.children.append(self.coinCount)

        self.world = TextObject(self, fontSpriteMap, "WORLD", 1)
        self.world.transform.translate(464, 568)
        self.world.transform.setScale(3, 3)
        self.children.append(self.world)

        self.worldStage = TextObject(self, fontSpriteMap,
            str(gameState.world) + "-" + str(gameState.stage), 1)
        self.worldStage.transform.translate(488, 544)
        self.worldStage.transform.setScale(3, 3)
        self.children.append(self.worldStage)

        self.time = TextObject(self, fontSpriteMap, "TIME", 1)
        self.time.transform.translate(640, 568)
        self.time.transform.setScale(3, 3)
        self.children.append(self.time)

        self.timeCount = TextObject(self, fontSpriteMap, str(gameState.time).zfill(3), 1)
        self.timeCount.transform.translate(656, 544)
        self.timeCount.transform.setScale(3, 3)
        self.children.append(self.timeCount)

    def update(self, deltaTime):
        super().update(deltaTime)

        self.name.setText(fontSpriteMap, self.gameState.name)
        self.score.setText(fontSpriteMap, str(self.gameState.score).zfill(6))
        self.coinCount.setText(fontSpriteMap, str(self.gameState.coin).zfill(2))
        self.worldStage.setText(fontSpriteMap,
            str(self.gameState.world) + "-" + str(self.gameState.stage))
        self.timeCount.setText(fontSpriteMap, str(self.gameState.time).zfill(3))


gameState = GameState(root)
gamePlayInterface = GamePlayInterface(root, gameState)

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

    pico2d.delay(max(0.0, 1 / TARGET_FPS - elapsedTime))

pico2d.close_canvas()