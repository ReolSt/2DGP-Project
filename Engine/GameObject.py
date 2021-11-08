import pico2d

import os
if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Singleton import *
    from Settings import *
    from Transform import *
    from RigidBody import *
else:
    from .Singleton import *
    from .Settings import *
    from .Transform import *
    from .RigidBody import *

from typing import Union, Callable, Iterable

class GameObjectIDGenerator(metaclass=Singleton):
    OBJECT_MAX_ID = int(Settings().default["GameObjectMaxId"])
    def __init__(self):
        """

        Returns
        -------
        None.

        """

        self.currentId = 0

    def generate(self):
        """
        Returns
        -------
        generated_id : int
            DESCRIPTION.

        """

        generated_id = self.currentId

        self.currentId = (self.currentId + 1) % GameObjectIDGenerator.OBJECT_MAX_ID
        return generated_id

class GameObject:
    def __init__(self, parent = None):
        """
        Parameters
        ----------
        parent : GameObject or Transform, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """

        if isinstance(parent, GameObject):
            self.transform = Transform(parent.transform, self)
        else:
            self.transform = Transform(parent, self)

        self.id = GameObjectIDGenerator().generate()

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
            "CollisionEnter": [],
            "CollisionStay": [],
        }

        self.keyDown = {}

        if self.transform.parent is not None:
            self.scene = self.transform.parent.gameObject.scene

        self.__layer = "Default"
        self.__rigidBody = None

    @property
    def layer(self):
        return self.__layer

    @layer.setter
    def layer(self, layer):
        assert isinstance(layer, str), "[GameObject] layer.setter : layer is not instance of str. ( layer = {} )".format(layer)

        self.__layer = layer

    @property
    def rigidBody(self):
        return self.__rigidBody

    @rigidBody.setter
    def rigidBody(self, rigidBody):
        assert hasattr(self, "scene"), "[GameObject] rigidBody.setter : object has no scene property."
        assert isinstance(rigidBody, RigidBody), \
            "[GameObject] rigidBody.setter : parameter is not instance of RigidBody. ( rigidBody = {} )".format(rigidBody)

        if self.__rigidBody is not None:
            self.scene.physicsManager.remove(self.__rigidBody)

        self.__rigidBody = rigidBody
        self.scene.physicsManager.add(self.__rigidBody)

    def captureEvent(self, event : pico2d.SDL_Event):
        """
        Parameters
        ----------
        event : SDL_Event
            DESCRIPTION.

        Returns
        -------
        None.

        """

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
            if event.key is None:
                for key in self.keyDown:
                    if self.keyDown[key]:
                        event.key = key
                        self.onKeyPress(event)
            elif event.key not in self.keyDown:
                self.keyDown[event.key] = False

            if not self.keyDown[event.key]:
                self.onKeyDown(event)
                self.keyDown[event.key] = True
        elif event.type == pico2d.SDL_KEYUP:
            if event.key == None:
                return

            if event.key not in self.keyDown:
                self.keyDown[event.key] = False
            self.keyDown[event.key] = False

            self.onKeyUp(event)

    def addEventListener(self, eventType : str, callback : Callable):
        """
        Parameters
        ----------
        eventType : str
            DESCRIPTION.
        callback : function
            DESCRIPTION.

        Returns
        -------
        None.

        """

        assert(eventType in self.eventListeners.keys())

        self.eventListeners[eventType].append(callback)

    def removeEventListeners(self, eventType : str):
        """
        Parameters
        ----------
        eventType : str
            DESCRIPTION.

        Returns
        -------
        None.

        """

        assert(eventType in self.eventListeners.keys())

        self.eventListeners[eventType] = []

    def update(self, deltaTime: float):
        """

        Parameters
        ----------
        deltaTime : float
            DESCRIPTION.

        Returns
        -------
        None.

        """

        for callback in self.eventListeners["Update"]:
            callback(self)

        for child in self.children:
            child.update(deltaTime)

        self.transform.update()

        if self.rigidBody is not None:
            self.rigidBody.update()

    def render(self, camera, debug : bool = False):
        if camera.layer == self.layer:
            for callback in self.eventListeners["Render"]:
                callback(self)

            for sprite in self.sprites:
                sprite.transform.update()
                sprite.render(camera)

            if debug and self.rigidBody is not None:
                self.rigidBody.render(camera)

        for child in self.children:
            child.render(camera, debug)

    def onMouseMove(self, event : pico2d.SDL_Event):
        for callback in self.eventListeners["MouseMove"]:
            callback(self, event)

        for child in self.children:
            child.onMouseMove(event)

    def onMouseDown(self, event : pico2d.SDL_Event):
        for callback in self.eventListeners["MouseDown"]:
            callback(self, event)

        for child in self.children:
            child.onMouseDown(event)

    def onMouseUp(self, event : pico2d.SDL_Event):
        for callback in self.eventListeners["MouseUp"]:
            callback(self, event)

        for child in self.children:
            child.onMouseUp(event)

    def onMouseWheel(self, event : pico2d.SDL_Event):
        for callback in self.eventListeners["MouseWheel"]:
            callback(self, event)

        for child in self.children:
            child.onMouseWheel(event)

    def onKeyDown(self, event : pico2d.SDL_Event):
        for callback in self.eventListeners["KeyDown"]:
            callback(self, event)

        for child in self.children:
            child.onKeyDown(event)

    def onKeyUp(self, event : pico2d.SDL_Event):
        for callback in self.eventListeners["KeyUp"]:
            callback(self, event)

        for child in self.children:
            child.onKeyUp(event)

    def onKeyPress(self, event : pico2d.SDL_Event):
        for callback in self.eventListeners["KeyPress"]:
            callback(self, event)

        for child in self.children:
            child.onKeyPress(event)

    def addChild(self, child):
        self.children.append(child)

        if child.rigidBody is not None:
            child.rigidBody.update()

    def addChildren(self, children):
        for child in children:
            self.children.append(child)

    def removeChild(self, chlid):
        self.children.remove(child)

    def removeChildren(self, children):
        for child in children:
            self.children.remove(child)

    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)