import pico2d
from Transform import *

class GameObject:
    def __init__(self, parent=None):
        if type(parent) is GameObject:
            parent = parent.transform
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
            "KeyUp": [],
        }

    def captureEvent(self, event):
        if event.type == pico2d.SDL_MOUSEBUTTONUP:
            self.onMouseUp(event)
        elif event.type == pico2d.SDL_MOUSEBUTTONDOWN:
            self.onMouseDown(event)
        elif event.type == pico2d.SDL_MOUSEMOTION:
            self.onMouseMove(event)
        elif event.type == pico2d.SDL_MOUSEWHEEL:
            self.onMouseWheel(event)
        elif event.type == pico2d.SDL_KEYDOWN:
            self.onKeyDown(event)
        elif event.type == pico2d.SDL_KEYUP:
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