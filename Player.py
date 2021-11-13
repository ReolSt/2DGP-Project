import pico2d

from Engine.Vector2 import Vector2
from Engine.GameObject import GameObject
from Engine.EntitySprite import EntitySprite
from Engine.RigidBody import RigidBody
from Engine.AudioMixer import AudioMixer

import pymunk

class Player(GameObject):
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

        self.running = False
        self.stopping = False

        self.direction = 1

        self.jumpPressing = False
        self.jumping = False
        self.longJumping = False

        self.died = False
        self.dieType = 0
        self.dieAnimationTimeStep = 0

        self.epsilon = 0.01

        self.direction = 1
        self.maxVelocity = Vector2(250, 700)
        self.acceleration = Vector2(0.5, 50.0)
        self.stoppingAcceleration = 1.0

        self.jumpStartVelocity = 300
        self.longJumpTime = 0
        self.longJumpDuration = 600
        self.longJumpAcceleration = 2.3

        self.runAnimationFrame = 1
        self.runAnimationInterval = 20000
        self.runAnimationFrameDuration = 0

        width = self.sprites[0].width
        height = self.sprites[0].height

        self.rigidBody = RigidBody(self)
        self.rigidBody.vertices = [(-width / 2, -height / 2), (width / 2, -height / 2), (width / 2, height / 2), (-width / 2, height / 2)]
        self.rigidBody.bodyType = "Dynamic"
        self.rigidBody.filter = 0b100
        self.rigidBody.mass = 1000
        self.rigidBody.moment = float('inf')
        self.rigidBody.elasticity = 0

    def switchSprite(self, spriteName):
        self.sprites[0] = self.animationSprites[spriteName]

    def dieAnimationYDelta(self, timeStep):
        if timeStep < 400 or timeStep > 1200 or timeStep == 800:
            return 0
        else:
            return (800 - timeStep) * 2

    def updateRunAnimation(self, deltaTime):
        if not self.jumping and self.running:
            self.transform.localFlip.x = self.direction < 0

        self.switchSprite("Stand")

        if self.rigidBody.velocityX != 0:
            if not self.jumping:
                self.switchSprite("Run" + str(self.runAnimationFrame))

            self.runAnimationFrameDuration += deltaTime * abs(self.rigidBody.velocityX)

            if self.runAnimationFrameDuration > self.runAnimationInterval:
                self.runAnimationFrame = (self.runAnimationFrame % 3) + 1
                self.runAnimationFrameDuration = 0.0

        if self.stopping and not self.jumping and self.direction * self.rigidBody.velocityX < 0:
            self.switchSprite("Kick")

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

    def startRunning(self, direction):
        if self.running and self.direction != direction:
            self.startStopping()

        self.running = True
        self.direction = direction

    def endRunning(self, direction):
        self.running = False if self.direction == direction else self.running
        self.startStopping()

    def startJumping(self):
        self.jumping = True
        self.jumpPressing = True
        self.rigidBody.velocityY = self.jumpStartVelocity

    def endJumping(self):
        self.jumpPressing = False
        self.longJumping = False
        self.longJumpTime = 0

    def startStopping(self):
        self.stopping = True

    def updateMovement(self, deltaTime):
        if self.died:
            return

        acceleration = self.acceleration * deltaTime

        if self.stopping:
            if self.rigidBody.velocityX > 0:
                self.rigidBody.velocityX -= self.stoppingAcceleration * deltaTime
                self.rigidBody.velocityX = max(0, self.rigidBody.velocityX)
            elif self.rigidBody.velocityX < 0:
                self.rigidBody.velocityX += self.stoppingAcceleration * deltaTime
                self.rigidBody.velocityX = min(0, self.rigidBody.velocityX)

            if self.rigidBody.velocityX == 0:
                self.stopping = False

        elif self.running:
            self.rigidBody.velocityX += acceleration.x * self.direction
            self.rigidBody.velocityX = max(-self.maxVelocity.x, self.rigidBody.velocityX)
            self.rigidBody.velocityX = min(self.maxVelocity.x, self.rigidBody.velocityX)

    def canJump(self):
        bb = self.rigidBody.bb
        shape = pymunk.Poly(pymunk.Body(), [(bb.left + 1, bb.bottom - 1), (bb.right - 1, bb.bottom - 1), (bb.right - 1, bb.bottom + 1), (bb.left + 1, bb.bottom + 1)])

        queryInfos = self.rigidBody.space.shape_query(shape)
        for queryInfo in queryInfos:
            shape = queryInfo.shape
            if shape.filter.categories & 0b1:
                return True

        return False

    def updateJumping(self, deltaTime):
        if self.died:
            return

        if self.jumpPressing:
            if self.longJumping:
                self.rigidBody.velocityY += self.longJumpAcceleration * deltaTime
                self.longJumpTime += deltaTime

                if self.longJumpTime >= self.longJumpDuration:
                    self.longJumpTime = 0
                    self.jumpPressing = False
                    self.longJumping = False
            else:
                self.rigidBody.velocityY += self.acceleration.y * deltaTime
                
                if self.rigidBody.velocityY >= self.maxVelocity.y:
                   self.longJumping = True        

        if self.jumping:
            if abs(self.rigidBody.velocityY) < self.epsilon and self.canJump():
                self.jumping = False
                self.rigidBody.velocityY = 0

    def updateDie(self, deltaTime):
        if self.transform.getPosition().y <= 0:
            self.died = True

        if self.died:
            self.rigidBody.bodyType = "Kinematic"
            self.dieAnimationTimeStep += deltaTime
            self.rigidBody.velocityY = self.dieAnimationYDelta(self.dieAnimationTimeStep)

    def update(self, deltaTime):
        super().update(deltaTime)

        self.updateAnimation(deltaTime)

        self.updateDie(deltaTime)
        self.updateJumping(deltaTime)
        self.updateMovement(deltaTime)

        self.rigidBody.angle = 0

        if self.died:
            return
