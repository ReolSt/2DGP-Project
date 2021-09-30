import pico2d

from GameObject import *
from EntitySprite import *

class Player(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.animationSprites = {
            "MarioStand": EntitySprite(self.transform, "MarioStand"),
            "MarioRun1": EntitySprite(self.transform, "MarioRun1"),
            "MarioRun2": EntitySprite(self.transform, "MarioRun2"),
            "MarioRun3": EntitySprite(self.transform, "MarioRun3"),
            "MarioJump": EntitySprite(self.transform, "MarioJump"),
            "MarioDead": EntitySprite(self.transform, "MarioDead"),
            "MarioKick": EntitySprite(self.transform, "MarioKick")
        }

        self.sprites = [self.animationSprites["MarioStand"]]

        self.input = True

        self.moveLeft = False
        self.moveRight = False

        self.runningAnimationFrame = 1

        self.stopping = False

        self.acceleration = 0.0005
        self.currentSpeed = 0.0
        self.minSpeed = 0.1
        self.maxSpeed = 0.3

    def onKeyDown(self, event):
        super().onKeyDown(event)

        if not self.input:
            return

        if event.key == pico2d.SDLK_LEFT:
            self.moveLeft = True
            self.transform.localFlip[0] = True
        elif event.key == pico2d.SDLK_RIGHT:
            self.moveRight = True
            self.transform.localFlip[0] = False

    def onKeyUp(self, event):
        super().onKeyUp(event)

        if not self.input:
            return

        if event.key == pico2d.SDLK_LEFT:
            self.moveLeft = False
            self.stopping = True
        elif event.key == pico2d.SDLK_RIGHT:
            self.moveRight = False
            self.stopping = True

    def update(self, deltaTime):
        super().update(deltaTime)

        acceleration = deltaTime * self.acceleration

        if self.moveLeft or self.moveRight or self.stopping:
            self.sprites = [self.animationSprites["MarioRun" + str(self.runningAnimationFrame)]]
            self.runningAnimationFrame = (self.runningAnimationFrame % 3) + 1

        if self.moveLeft:
            if self.stopping and self.currentSpeed >= 0:
                self.sprites = [self.animationSprites["MarioKick"]]
            self.currentSpeed = max(-self.maxSpeed, self.currentSpeed - acceleration)
        elif self.moveRight:
            if self.stopping and self.currentSpeed <= 0:
                self.sprites = [self.animationSprites["MarioKick"]]
            self.currentSpeed = min(self.maxSpeed, self.currentSpeed + acceleration)

        if self.stopping:
            if self.currentSpeed > 0:
                self.currentSpeed = max(0.0, self.currentSpeed - acceleration)
            elif self.currentSpeed < 0:
                self.currentSpeed = min(0.0, self.currentSpeed + acceleration)

            if self.currentSpeed == 0:
                self.stopping = False
                self.sprites = [self.animationSprites["MarioStand"]]

        self.transform.translate(deltaTime * self.currentSpeed, 0)