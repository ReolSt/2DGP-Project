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

        self.moving = 0
        self.stopping = False

        self.jumpPressing = True
        self.jumping = False

        self.speed = [0.0, 0.0]
        self.minSpeed = [0.0, 0.2]
        self.maxSpeed = [0.3, 0.5]
        self.acceleration = [0.0005, 0.003]
        self.gravity = 0.0015

        self.runningAnimationFrame = 1
        self.runningAnimationInterval = 20.0
        self.runningAnimationFrameDuration = 0.0

        self.collider = BoxCollider(
            self.transform, self.sprites[0].width, self.sprites[0].height)

    def onKeyDown(self, event):
        super().onKeyDown(event)

        if not self.input:
            return

        if event.key == pico2d.SDLK_LEFT:
            self.moving = -1
        elif event.key == pico2d.SDLK_RIGHT:
            self.moving = 1
        elif event.key == pico2d.SDLK_SPACE:
            if not self.jumping:
                self.jumping = True
                self.jumpPressing = True
                self.speed[1] = self.minSpeed[1]

    def onKeyPress(self, event):
        super().onKeyPress(event)

        if not self.input:
            return

    def onKeyUp(self, event):
        super().onKeyUp(event)

        if not self.input:
            return

        if event.key == pico2d.SDLK_LEFT:
            self.moving = 0 if self.moving == -1 else self.moving
            self.stopping = True
        elif event.key == pico2d.SDLK_RIGHT:
            self.moving = 0 if self.moving == 1 else self.moving
            self.stopping = True
        elif event.key == pico2d.SDLK_SPACE:
            self.jumpPressing = False

    def updateAnimation(self, deltaTime):
        if not self.jumping and self.moving:
            self.transform.localFlip[0] = self.moving < 0

        if self.moving != 0 or self.stopping:
            if not self.jumping:
                self.sprites[0] = self.animationSprites["Run" + str(self.runningAnimationFrame)]

            self.runningAnimationFrameDuration += deltaTime * abs(self.speed[0])

            if self.runningAnimationFrameDuration > self.runningAnimationInterval:
                self.runningAnimationFrame = (self.runningAnimationFrame % 3) + 1
                self.runningAnimationFrameDuration = 0.0

        if self.stopping and not self.jumping and self.moving * self.speed[0] < 0.0:
            self.sprites[0] = self.animationSprites["Kick"]

        if (self.moving == 0 or self.stopping) and self.speed[0] == 0.0:
            self.sprites[0] = self.animationSprites["Stand"]

        if self.jumping:
            self.sprites[0] = self.animationSprites["Jump"]

            if not self.jumpPressing and self.transform.localPosition[1] <= 100.0:
                self.sprites[0] = self.animationSprites["Stand"]

    def updateMove(self, deltaTime):
        acceleration = deltaTime * self.acceleration[0]
        gravity = deltaTime * self.gravity

        if self.moving != 0:
            self.speed[0] += acceleration * self.moving
            self.speed[0] = max(-self.maxSpeed[0], self.speed[0])
            self.speed[0] = min(self.maxSpeed[0], self.speed[0])
        elif self.stopping:
            if self.speed[0] > 0:
                self.speed[0] -= acceleration
                self.speed[0] = max(0.0, self.speed[0])
            elif self.speed[0] < 0:
                self.speed[0] += acceleration
                self.speed[0] = min(0.0, self.speed[0])

            self.stopping = False if self.speed[0] == 0.0 else self.stopping

    def updateJump(self, deltaTime):
        acceleration = deltaTime * self.acceleration[1]
        gravity = deltaTime * self.gravity

        if self.jumping:
            self.speed[1] -= gravity
            if self.jumpPressing:
                self.speed[1] += acceleration

                if self.speed[1] >= self.maxSpeed[1]:
                    self.jumpPressing = False

                self.speed[1] = min(self.speed[1], self.maxSpeed[1])

            if not self.jumpPressing and self.transform.localPosition[1] <= 100.0:
                self.jumping = False
                self.speed[1] = 0.0
                self.transform.localPosition[1] = 100.0

    def update(self, deltaTime):
        super().update(deltaTime)

        self.updateAnimation(deltaTime)
        self.updateJump(deltaTime)
        self.updateMove(deltaTime)

        self.transform.translate(deltaTime * self.speed[0],
                                 deltaTime * self.speed[1])

    def onCollisionEnter(self, collider):
        if self.jumping and not self.jumpPressing:
            self.jumping = False
            self.speed[1] = 0.0