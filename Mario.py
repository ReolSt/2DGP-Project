import pico2d

from Engine.Vector2 import *
from Engine.GameObject import *
from Engine.EntitySprite import *
from Engine.RigidBody import *
from Engine.AudioMixer import *

import pymunk

class Mario(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.animationSprites = {
            "Stand": EntitySprite(self, "MarioStand"),
            "Run1": EntitySprite(self, "MarioRun1"),
            "Run2": EntitySprite(self, "MarioRun2"),
            "Run3": EntitySprite(self, "MarioRun3"),
            "Jump": EntitySprite(self, "MarioJump"),
            "Die": EntitySprite(self, "MarioDie"),
            "Kick": EntitySprite(self, "MarioKick")
        }

        self.sprites = [self.animationSprites["Stand"]]

        self.moving = False
        self.stopping = False

        self.direction = 1

        self.jumpPressing = False
        self.jumping = False

        self.died = False
        self.dieAnimationTimeStep = 0

        self.epsilon = 0.01

        self.direction = 1
        self.maxVelocity = Vector2(120, 150)
        self.acceleration = Vector2(0.1, 1.5)

        self.runAnimationFrame = 1
        self.runAnimationInterval = 10000.0
        self.runAnimationFrameDuration = 0.0

        body = pymunk.Body()
        shape = pymunk.Poly.create_box(body, (self.sprites[0].width, self.sprites[0].height))

        self.rigidBody = RigidBody(self, body, shape)
        self.rigidBody.bodyType = "Dynamic"
        self.rigidBody.filter = 0b1
        self.rigidBody.mass = 1000
        self.rigidBody.moment = float('inf')
        self.rigidBody.elasticity = 0
        self.rigidBody.friction = 1

    def switchSprite(self, spriteName):
        self.sprites[0] = self.animationSprites[spriteName]

    def dieAnimationYDelta(self, timeStep):
        if timeStep < 400:
            return 0
        else:
            return 400 / 160000 * (800 - timeStep)

    def updateRunAnimation(self, deltaTime):
        if not self.jumping and self.moving:
            self.transform.localFlip.x = self.direction < 0

        if self.moving or self.stopping:
            if not self.jumping:
                self.switchSprite("Run" + str(self.runAnimationFrame))

            self.runAnimationFrameDuration += deltaTime * abs(self.rigidBody.velocityX)

            if self.runAnimationFrameDuration > self.runAnimationInterval:
                self.runAnimationFrame = (self.runAnimationFrame % 3) + 1
                self.runAnimationFrameDuration = 0.0

        if self.stopping and not self.jumping and self.moving and self.direction * self.rigidBody.velocityX < 0:
            self.switchSprite("Kick")

        if (not self.moving or self.stopping) and self.rigidBody.velocityX == 0.0:
            self.switchSprite("Stand")

    def updateJumpAnimation(self, deltaTime):
        if self.jumping:
            self.switchSprite("Jump")

    def updateDieAnimation(self, deltaTime):
        if self.died:
            self.switchSprite("Die")
            return

    def updateAnimation(self, deltaTime):
        self.updateRunAnimation(deltaTime)
        self.updateJumpAnimation(deltaTime)
        self.updateDieAnimation(deltaTime)

    def updateMove(self, deltaTime):
        if self.died:
            return

        acceleration = self.acceleration * deltaTime

        if self.moving:
            self.rigidBody.velocityX += acceleration.x * self.direction
            self.rigidBody.velocityX = max(-self.maxVelocity.x, self.rigidBody.velocityX)
            self.rigidBody.velocityX = min(self.maxVelocity.x, self.rigidBody.velocityX)
        elif self.stopping:
            if self.rigidBody.velocityX > 0:
                self.rigidBody.velocityX -= acceleration.x
                self.rigidBody.velocityX = max(0.0, self.rigidBody.velocityX)
            elif self.rigidBody.velocityX < 0:
                self.rigidBody.velocityX += acceleration.x
                self.rigidBody.velocityX = min(0.0, self.rigidBody.velocityX)


    def runStart(self, direction):
        if direction > 0:
            pass
        elif direction < 0:
            pass

    def updateJump(self, deltaTime):
        if self.died:
            return

        acceleration = self.acceleration * deltaTime

        if self.jumpPressing:
            self.rigidBody.velocityY += acceleration.y

            if self.rigidBody.velocityY > self.maxVelocity.y:
                self.jumpPressing = False
                self.rigidBody.velicityY = self.maxVelocity.y

    def updateDie(self, deltaTime):
        if self.died:
            self.dieAnimationTimeStep += deltaTime
            self.transform.translate(0.0, self.dieAnimationYDelta(self.dieAnimationTimeStep))

    def update(self, deltaTime):
        self.updateAnimation(deltaTime)

        self.updateDie(deltaTime)
        self.updateJump(deltaTime)
        self.updateMove(deltaTime)

        self.rigidBody.angle = 0

        if self.died:
            return

        if self.jumping:
            if abs(self.rigidBody.body.velocity.y) < self.epsilon:
                self.jumping = False
                self.rigidBody.body.velocity = pymunk.vec2d.Vec2d(self.rigidBody.body.velocity.x, 0)

        if self.transform.position.y < 0.0:
            self.died = True

        super().update(deltaTime)