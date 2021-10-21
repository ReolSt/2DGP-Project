import pico2d

from Engine.Vector2 import *
from Engine.GameObject import *
from Engine.EntitySprite import *
from Engine.BoxCollider import *
from Engine.AudioMixer import *

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

        self.moving = 0
        self.stopping = False

        self.jumpPressing = True
        self.jumping = False

        self.died = False
        self.dieAnimationTimeStep = 0

        self.speed = Vector2(0.0, 0.0)
        self.minSpeed = Vector2(0.0, 0.2)
        self.maxSpeed = Vector2(0.3, 0.4)
        self.acceleration = Vector2(0.0005, 0.003)
        self.gravity = 0.0015

        self.runAnimationFrame = 1
        self.runAnimationInterval = 20.0
        self.runAnimationFrameDuration = 0.0

        collider = BoxCollider(self, self.sprites[0].width, self.sprites[0].height)

        self.addCollider(collider)

    def switchSprite(self, spriteName):
        self.sprites[0] = self.animationSprites[spriteName]

    def dieAnimationYDelta(self, timeStep):
        if timeStep < 400:
            return 0
        else:
            return 400 / 160000 * (800 - timeStep)

    def updateRunAnimation(self, deltaTime):
        if not self.jumping and self.moving:
            self.transform.localFlip.x = self.moving < 0

        if self.moving != 0 or self.stopping:
            if not self.jumping:
                self.switchSprite("Run" + str(self.runAnimationFrame))

            self.runAnimationFrameDuration += deltaTime * abs(self.speed.x)

            if self.runAnimationFrameDuration > self.runAnimationInterval:
                self.runAnimationFrame = (self.runAnimationFrame % 3) + 1
                self.runAnimationFrameDuration = 0.0

        if self.stopping and not self.jumping and self.moving * self.speed.x < 0.0:
            self.switchSprite("Kick")

        if (self.moving == 0 or self.stopping) and self.speed.x == 0.0:
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
        if self.died:
            return

        acceleration = deltaTime * self.acceleration.y

        if self.jumping:
            if self.jumpPressing:
                self.speed.y += acceleration

                if self.speed.y >= self.maxSpeed.y:
                    self.jumpPressing = False

                self.speed.y = min(self.speed.y, self.maxSpeed.y)

    def updateDie(self, deltaTime):
        if self.died:
            self.dieAnimationTimeStep += deltaTime
            self.transform.translate(0.0, self.dieAnimationYDelta(self.dieAnimationTimeStep))


    def update(self, deltaTime):
        super().update(deltaTime)

        self.updateAnimation(deltaTime)

        self.updateDie(deltaTime)
        self.updateJump(deltaTime)
        self.updateMove(deltaTime)

        if self.died:
            return

        position = self.transform.position
        scale = self.transform.scale
        rayDistance = Vector2(
            self.sprites[0].width * scale.x / 2,
            self.sprites[0].height * scale.y / 2)

        floorHit = self.scene.collisionManager.rayCast(
            origin=position,
            direction=Vector2(0.0, -1.0),
            distance=rayDistance.y,
            tag="Floor")

        gravity = deltaTime * self.gravity

        if self.speed.x < 0:
            leftHit = self.scene.collisionManager.rayCast(
                origin=position,
                direction=Vector2(-1.0, 0.0),
                distance=rayDistance.x,
                tag="Floor")

            if leftHit is not None:
                self.speed.x = 0

        if self.speed.x > 0:
            rightHit = self.scene.collisionManager.rayCast(
                    origin=position,
                    direction=Vector2(1.0, 0.0),
                    distance=rayDistance.x,
                    tag="Floor")

            if rightHit is not None:
                self.speed.x = 0

        if floorHit is None:
            self.speed.y -= gravity
        else:
            if self.jumping and self.speed.y < 0:
                self.jumping = False
                self.switchSprite("Stand")

            if not self.jumping:
                self.speed.y = 0.0

        if self.speed.y > 0:
            ceilHit = self.scene.collisionManager.rayCast(
                origin=position,
                direction=Vector2(0.0, 1.0),
                distance=rayDistance.y,
                tag="Floor")

            if ceilHit is not None:
                self.speed.y = 0
                self.jumpPressing = False

        if self.transform.position.y < 0.0:
            self.died = True

        self.transform.translate(deltaTime * self.speed.x,
                                 deltaTime * self.speed.y)