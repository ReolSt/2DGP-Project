import numpy

class Transform:
    def __init__(self, parent=None):
        assert(parent is Transform or parent is None)
        self.parent = parent

        self.position = [0.0, 0.0]
        self.rotation = 0.0
        self.scale = [1.0, 1.0]

        self.flip = False

    def localPosition(self):
        return self.position

    def localRotation(self):
        return self.rotation

    def localScale(self):
        return self.scale

    def localFlip(self):
        return self.flip

    def position(self):
        parent = self.parent
        position = self.position
        while parent is not None:
            parent_position = parent.position
            parent_rotation = parent.rotation
            parent_scale = parent.scale
            parent_flip = parent.flip

            position *= parent_scale

            position[0] *= numpy.cos(numpy.deg2rad(parent_rotation))
            position[1] *= numpy.sin(numpy.deg2rad(parent_rotation))

            position += parent_position

        return position

    def rotation(self):
        parent = self.parent
        rotation = self.rotation
        while parent is not None:
            rotation += parent.rotation

        return rotation

    def scale(self):
        parent = self.parent
        scale = self.scale
        while parent is not None:
            scale *= parent.scale

        return scale

    def flip(self):
        parent = self.parent
        flip = self.flip
        while parent is not None:
            if parent.flip:
                flip = not flip

        return flip