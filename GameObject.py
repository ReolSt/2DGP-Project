import Transform

class GameObject:
    def __init__(self, parent=None):
        self.transform = Transform(parent)
        self.transform.parent = parent

        self.children = []

    def attach_sprite(self, sprite):
        self.sprite = sprite

    def update(self, deltaTime):
        for child in self.children:
            child.update(deltaTime)

    def render(self):
        for child in self.children:
            child.render()

    def onMouseMove(self, event):
        for child in self.children:
            child.onMouseMove()

    def onMouseDown(self, event):
        for child in self.children:
            child.onMouseDown(event)

    def onMouseUp(self, event):
        for child in self.children:
            child.onMouseUp(event)

    def onMouseWheel(self, event):
        for child in self.children:
            child.onMouseWheel(event)

    def onKeyDown(self, event):
        for child in self.children:
            child.onKeyDown(event)

    def onKeyUp(self, event):
        for child in self.children:
            child.onKeyUp(event)