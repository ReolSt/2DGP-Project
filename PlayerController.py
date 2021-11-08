from Engine.GameObject import *
from Engine.AudioMixer import *
from Engine.Settings import *

from Mario import *

class PlayerController(GameObject):
    def __init__(self, parent, camera):
        super().__init__(parent)

        self.player = Mario(self)
        self.camera = camera

        self.addChild(self.player)

        self.input = True

    def update(self, deltaTime):
        super().update(deltaTime)

        cameraPosition = self.camera.transform.position
        playerPosition = self.player.transform.position

        if playerPosition.x - cameraPosition.x < 100.0:
            self.camera.transform.translate(playerPosition.x - cameraPosition.x - 100.0, 0)
        elif playerPosition.x - cameraPosition.x > 300.0:
            self.camera.transform.translate(playerPosition.x - cameraPosition.x - 300.0, 0)

    def onKeyDown(self, event):
        super().onKeyDown(event)

        if not self.input:
            return

        if self.player.died:
            return

        if event.key == pico2d.SDLK_LEFT:
            self.player.moving = True
            self.player.direction = -1
        elif event.key == pico2d.SDLK_RIGHT:
            self.player.moving = True
            self.player.direction = 1
        elif event.key == pico2d.SDLK_SPACE:
            if not self.player.jumping:
                self.player.jumping = True
                self.player.jumpPressing = True

                AudioMixer().playWav("JumpSmall")

    def onKeyPress(self, event):
        super().onKeyPress(event)

        if not self.input:
            return

    def onKeyUp(self, event):
        super().onKeyUp(event)

        if not self.input:
            return

        if event.key == pico2d.SDLK_LEFT:
            self.player.moving = False if self.player.direction == -1 else self.player.moving
            self.player.stopping = True
        elif event.key == pico2d.SDLK_RIGHT:
            self.player.moving = False if self.player.direction == 1 else self.player.moving
            self.player.stopping = True
        elif event.key == pico2d.SDLK_SPACE:
            self.player.jumpPressing = False