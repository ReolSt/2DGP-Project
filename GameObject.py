import pico2d

from Settings import *
from Transform import *

class GameObject:
    def __init__(self, parent=None):
        if isinstance(parent, GameObject):
            self.transform = Transform(parent.transform)
        else:
            self.transform = Transform(parent)

        self.children = []
        self.sprites = []

        self.eventListeners = {
            "Update": [],
            "Render": [],
            "MouseMove": [],
            "MouseDown": [],
            "MouseUp": [],
            "MouseWheel": [],
            "KeyDown": [],
            "KeyPress": [],
            "KeyUp": [],
        }

        self.keyDown = {}

    def captureEvent(self, event):

        if event.type == pico2d.SDL_MOUSEBUTTONUP:
            event.y = int(Settings().default["WindowHeight"]) - 1 - event.y
            self.onMouseUp(event)
        elif event.type == pico2d.SDL_MOUSEBUTTONDOWN:
            event.y = int(Settings().default["WindowHeight"]) - 1 - event.y
            self.onMouseDown(event)
        elif event.type == pico2d.SDL_MOUSEMOTION:
            event.y = int(Settings().default["WindowHeight"]) - 1 - event.y
            self.onMouseMove(event)
        elif event.type == pico2d.SDL_MOUSEWHEEL:
            event.y = int(Settings().default["WindowHeight"]) - 1 - event.y
            self.onMouseWheel(event)
        elif event.type == pico2d.SDL_KEYDOWN:
            if event.key not in self.keyDown:
                self.keyDown[event.key] = False

            if self.keyDown[event.key]:
                self.onKeyPress(event)
            else:
                self.onKeyDown(event)
                self.keyDown[event.key] = True
        elif event.type == pico2d.SDL_KEYUP:
            if event.key not in self.keyDown:
                self.keyDown[event.key] = False
            self.keyDown[event.key] = False

            self.onKeyUp(event)

    def addEventListener(self, eventType, callback):
        self.eventListener[eventType].append(callback)

    def update(self, deltaTime):
        for callback in self.eventListeners["Update"]:
            callback(self)

        for child in self.children:
            child.update(deltaTime)

    def render(self):
        for callback in self.eventListeners["Render"]:
            callback(self)

        for sprite in self.sprites:
            sprite.render()

        for child in self.children:
            child.render()

    def onMouseMove(self, event):
        for callback in self.eventListeners["MouseMove"]:
            callback(self, event)

        for child in self.children:
            child.onMouseMove(event)

    def onMouseDown(self, event):
        for callback in self.eventListeners["MouseDown"]:
            callback(self, event)

        for child in self.children:
            child.onMouseDown(event)

    def onMouseUp(self, event):
        for callback in self.eventListeners["MouseUp"]:
            callback(self, event)

        for child in self.children:
            child.onMouseUp(event)

    def onMouseWheel(self, event):
        for callback in self.eventListeners["MouseWheel"]:
            callback(self, event)

        for child in self.children:
            child.onMouseWheel(event)

    def onKeyDown(self, event):
        for callback in self.eventListeners["KeyDown"]:
            callback(self, event)

        for child in self.children:
            child.onKeyDown(event)

    def onKeyUp(self, event):
        for callback in self.eventListeners["KeyUp"]:
            callback(self, event)

        for child in self.children:
            child.onKeyUp(event)

    def onKeyPress(self, event):
        for callback in self.eventListeners["KeyPress"]:
            callback(self, event)

        for child in self.children:
            child.onKeyPress(event)