import pico2d

from Engine.GameObject import *
from Engine.EntitySprite import *
from Engine.BoxCollider import *

class Player(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.animationSprites = {
            "Stand": EntitySprite(self.transform, "MarioStand"),
            "Run1": EntitySprite(self.transform, "MarioRun1"),
            "Run2": EntitySprite(self.transform, "MarioRun2"),
            "Run3": EntitySprite(self.transform, "MarioRun3"),
            "Jump": EntitySprite(self.transform, "MarioJump"),
            "Dead": EntitySprite(self.transform, "MarioDead"),
            "Kick": EntitySprite(self.transform, "MarioKick")
        }

        self.sprites = [self.animationSprites["Stand"]]

        self.input = True

        self.moveLeft = False
        self.moveRight = False

        self.runningAnimationFrame = 1

        self.stopping = False

        self.acceleration = 0.0005
        self.horizontalSpeed = 0.0
        self.maxHorizontalSpeed = 0.3

        self.moveAnimationInterval = 20.0
        self.moveAnimationFrameDuration = 0.0

        self.jumpPressing = True
        self.jumping = False

        self.verticalAcceleration = 0.003
        self.gravity = 0.0015
        self.verticalSpeed = 0.0
        self.maxVerticalSpeed = 0.50

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
        elif event.key == pico2d.SDLK_SPACE:
            if not self.jumping:
                self.jumping = True
                self.jumpPressing = True

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
        elif event.key == pico2d.SDLK_SPACE:
            self.jumpPressing = False

    def update(self, deltaTime):
        super().update(deltaTime)

        horizontalAcceleration = deltaTime * self.acceleration
        verticalAcceleration = deltaTime * self.verticalAcceleration
        gravity = deltaTime * self.gravity

        if self.jumping:
            self.sprites[0] = self.animationSprites["Jump"]
            if self.jumpPressing:
                self.verticalSpeed += verticalAcceleration

                if self.verticalSpeed >= self.maxVerticalSpeed:
                    self.jumpPressing = False

                self.verticalSpeed = min(self.verticalSpeed,
                                         self.maxVerticalSpeed)
            else:
                self.verticalSpeed -= gravity

            if not self.jumpPressing and self.transform.localPosition[1] <= 100.0:
                self.sprites[0] = self.animationSprites["Stand"]
                self.jumping = False
                self.verticalSpeed = 0.0
                self.transform.localPosition[1] = 100.0

        if self.moveLeft or self.moveRight or self.stopping:
            if not self.jumping:
                self.sprites[0] = self.animationSprites["Run" + str(self.runningAnimationFrame)]
            self.moveAnimationFrameDuration += deltaTime * abs(self.horizontalSpeed)

            if self.moveAnimationFrameDuration > self.moveAnimationInterval:
                self.runningAnimationFrame = (self.runningAnimationFrame % 3) + 1
                self.moveAnimationFrameDuration = 0.0

            if self.moveLeft:
                if self.stopping and self.horizontalSpeed >= 0 and not self.jumping:
                    self.sprites[0] = self.animationSprites["Kick"]
                self.horizontalSpeed -= horizontalAcceleration
                self.horizontalSpeed = max(-self.maxHorizontalSpeed,
                                           self.horizontalSpeed)
            elif self.moveRight:
                if self.stopping and self.horizontalSpeed <= 0 and not self.jumping:
                    self.sprites[0] = self.animationSprites["Kick"]
                self.horizontalSpeed += horizontalAcceleration
                self.horizontalSpeed = min(self.maxHorizontalSpeed,
                                           self.horizontalSpeed)
            elif self.stopping:
                if self.horizontalSpeed > 0:
                    self.horizontalSpeed -= horizontalAcceleration
                    self.horizontalSpeed = max(0.0, self.horizontalSpeed)
                elif self.horizontalSpeed < 0:
                    self.horizontalSpeed += horizontalAcceleration
                    self.horizontalSpeed = min(0.0, self.horizontalSpeed)

                if self.horizontalSpeed == 0:
                    self.stopping = False
                    self.sprites[0] = self.animationSprites["Stand"]

        self.transform.translate(deltaTime * self.horizontalSpeed,
                                 deltaTime * self.verticalSpeed)