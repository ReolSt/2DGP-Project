import pico2d

from Engine.Vector2 import *
from Engine.GameObject import *
from Engine.EntitySprite import *
from Engine.BoxCollider import *

from Engine.AudioMixer import *

class Player(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.animationSprites = {
            "Stand": EntitySprite(self, "MarioStand"),
            "Run1": EntitySprite(self, "MarioRun1"),
            "Run2": EntitySprite(self, "MarioRun2"),
            "Run3": EntitySprite(self, "MarioRun3"),
            "Jump": EntitySprite(self, "MarioJump"),
            "Dead": EntitySprite(self, "MarioDead"),
            "Kick": EntitySprite(self, "MarioKick")
        }

        self.sprites = [self.animationSprites["Stand"]]

        self.input = True

        self.moving = 0
        self.stopping = False

        self.jumpPressing = True
        self.jumping = False

        self.speed = Vector2(0.0, 0.0)
        self.minSpeed = Vector2(0.0, 0.2)
        self.maxSpeed = Vector2(0.3, 0.5)
        self.acceleration = Vector2(0.0005, 0.003)
        self.gravity = 0.0015

        self.runningAnimationFrame = 1
        self.runningAnimationInterval = 20.0
        self.runningAnimationFrameDuration = 0.0

        self.collider = BoxCollider(self.transform, self.sprites[0].width, self.sprites[0].height)

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
                self.speed.y = self.minSpeed.y


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

    def switchSprite(self, spriteName):
        self.sprites[0] = self.animationSprites[spriteName]

    def updateAnimation(self, deltaTime):
        if not self.jumping and self.moving:
            self.transform.localFlip.x = self.moving < 0

        if self.moving != 0 or self.stopping:
            if not self.jumping:
                self.switchSprite("Run" + str(self.runningAnimationFrame))

            self.runningAnimationFrameDuration += deltaTime * abs(self.speed.x)

            if self.runningAnimationFrameDuration > self.runningAnimationInterval:
                self.runningAnimationFrame = (self.runningAnimationFrame % 3) + 1
                self.runningAnimationFrameDuration = 0.0

        if self.stopping and not self.jumping and self.moving * self.speed.x < 0.0:
            self.switchSprite("Kick")

        if (self.moving == 0 or self.stopping) and self.speed.x == 0.0:
            self.switchSprite("Stand")

        if self.jumping:
            self.switchSprite("Jump")

    def updateMove(self, deltaTime):
        acceleration = deltaTime * self.acceleration.x
        gravity = deltaTime * self.gravity

        if self.moving != 0:
            self.speed.x += acceleration * self.moving
            self.speed.x = max(-self.maxSpeed.x, self.speed.x)
            self.speed.x = min(self.maxSpeed.x, self.speed.x)
        elif self.stopping:
            if self.speed.x > 0:
                self.speed.x -= acceleration
                self.speed.x = max(0.0, self.speed.x)
            elif self.speed.x < 0:
                self.speed.x += acceleration
                self.speed.x = min(0.0, self.speed.x)

            self.stopping = False if self.speed.x == 0.0 else self.stopping

    def updateJump(self, deltaTime):
        acceleration = deltaTime * self.acceleration.y
        gravity = deltaTime * self.gravity

        if self.jumping:
            self.speed.y -= gravity
            if self.jumpPressing:
                self.speed.y += acceleration

                if self.speed.y >= self.maxSpeed.y:
                    self.jumpPressing = False

                self.speed.y = min(self.speed.y, self.maxSpeed.y)

    def update(self, deltaTime):
        super().update(deltaTime)

        self.updateAnimation(deltaTime)
        self.updateJump(deltaTime)
        self.updateMove(deltaTime)

        self.transform.translate(deltaTime * self.speed.x,
                                 deltaTime * self.speed.y)

    def onCollisionEnter(self, collision):
        if collision.collider.tag == "ground" and self.jumping and not self.jumpPressing:
            self.jumping = False
            self.speed.y = 0.0
            self.switchSprite("Stand")