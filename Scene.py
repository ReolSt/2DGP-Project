import GameObject

class Scene:
    def __init__(self, name=""):
        self.name = name
        self.root = GameObject(None)
