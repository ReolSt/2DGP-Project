import numpy

class Transform:
    def __init__(self, parent=None):
        assert(isinstance(parent, Transform) or parent is None)

        self.parent = parent

        self.localPosition = numpy.array([0.0, 0.0])
        self.localRotation = 0.0
        self.localScale = numpy.array([1.0, 1.0])

        self.localFlip = numpy.array([False, False])

    def translate(self, x, y):
        self.localPosition += numpy.array([x, y], dtype=numpy.float32)

    def rotate(self, deg):
        self.localRotation += deg

    def setScale(self, xScale, yScale):
        self.localScale = numpy.array([xScale, yScale], dtype=numpy.float32)

    def position(self):
        parent = self.parent
        position = self.localPosition.copy()
        if parent is not None:
            parent_position = parent.position()
            parent_rotation = parent.rotation()
            parent_scale = parent.scale()

            position *= parent_scale

            cos = numpy.cos(numpy.deg2rad(parent_rotation))
            sin = numpy.sin(numpy.deg2rad(parent_rotation))

            position = numpy.array([position[0] * cos - position[1] * sin,
                                    position[1] * cos + position[0] * sin])

            position += parent_position

        return position

    def rotation(self):
        rotation = self.localRotation
        if self.parent is not None:
            rotation += self.parent.rotation()

        return rotation

    def scale(self):
        scale = self.localScale.copy()
        if self.parent is not None:
            scale *= self.parent.scale()

        return scale

    def flip(self):
        flip = self.localFlip.copy()
        if self.parent is not None:
            parent_flip = self.parent.flip()
            if parent_flip[0]:
                flip[0] = not flip[0]
            if parent_flip[1]:
                flip[1] = not flip[1]

        return flip