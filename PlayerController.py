import pico2d

from Engine.GameObject import GameObject
from Engine.AudioMixer import AudioMixer
from Engine.Settings import Settings

from Player import Player

class PlayerController(GameObject):
    def __init__(self, parent, camera):
        super().__init__(parent)

        self.player = Player(self)
        self.camera = camera

        self.addChild(self.player)

        self.input = True
        self.ended = False

    def update(self, deltaTime):
        super().update(deltaTime)

        cameraPosition = self.camera.transform.position
        playerPosition = self.player.transform.position

        if playerPosition.x - cameraPosition.x < 100.0:
            self.camera.transform.translate(playerPosition.x - cameraPosition.x - 100.0, 0)
        elif playerPosition.x - cameraPosition.x > 300.0:
            self.camera.transform.translate(playerPosition.x - cameraPosition.x - 300.0, 0)

        if self.player.died and not self.ended:
            AudioMixer().playWav("MarioDie")
            self.ended = True

    def onKeyDown(self, event):
        super().onKeyDown(event)

        if not self.input:
            return

        if self.player.died:
            return

        if event.key == pico2d.SDLK_LEFT:
            self.player.startRunning(-1)
        elif event.key == pico2d.SDLK_RIGHT:
            self.player.startRunning(1)
        elif event.key == pico2d.SDLK_SPACE:
            if self.player.canJump() and not self.player.jumping:
                self.player.startJumping()

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
            self.player.endRunning(-1)
        elif event.key == pico2d.SDLK_RIGHT:
            self.player.endRunning(1)
        elif event.key == pico2d.SDLK_SPACE:
            self.player.endJumping()