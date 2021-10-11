from Engine.GameObject import *
from Engine.AudioMixer import *

from Mario import *

class PlayerController(GameObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.player = Mario(self)
        self.children.append(self.player)

        self.input = True

    def onKeyDown(self, event):
        super().onKeyDown(event)

        if not self.input:
            return

        if event.key == pico2d.SDLK_LEFT:
            self.player.moving = -1
        elif event.key == pico2d.SDLK_RIGHT:
            self.player.moving = 1
        elif event.key == pico2d.SDLK_SPACE:
            if not self.player.jumping:
                self.player.jumping = True
                self.player.jumpPressing = True
                self.player.speed.y = self.player.minSpeed.y

                AudioMixer().play("JumpSmall")

    def onKeyPress(self, event):
        super().onKeyPress(event)

        if not self.input:
            return

    def onKeyUp(self, event):
        super().onKeyUp(event)

        if not self.input:
            return

        if event.key == pico2d.SDLK_LEFT:
            self.player.moving = 0 if self.player.moving == -1 else self.player.moving
            self.player.stopping = True
        elif event.key == pico2d.SDLK_RIGHT:
            self.player.moving = 0 if self.player.moving == 1 else self.player.moving
            self.player.stopping = True
        elif event.key == pico2d.SDLK_SPACE:
            self.player.jumpPressing = False