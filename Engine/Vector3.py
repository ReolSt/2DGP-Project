class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        """
        Parameters
        ----------
        x : float, optional
            The default is 0.0.
        y : float, optional
            The default is 0.0.
        z : float, optional
            The default is 0.0.

        Returns
        -------
        None.

        """

        self.x = x
        self.y = y
        self.z = z

    def copy(self):
        return __class__(self.x, self.y, self.z)

    def normalize(self):
        length = abs(self)
        return Vector3(self.x / length, self.y / length, self.z / length)

    def cross(self, other):
        if hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            return Vector3(self.y * other.z - self.z * other.y,
                           self.z * other.x - self.x * other.z,
                           self.x * other.y - self.y * other.x)

        assert False, "Invalid operand type"

    def assertIfInvalid(other):
        assert hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'), "Invalid operand type: {}".format(other)

    def __eq__(self, other):
        self.assertIfInvalid(other)

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        self.assertIfInvalid(other)

        return self.x != other.x or self.y != other.y or self.z != other.z

    def __ge__(self, other):
        self.assertIfInvalid(other)

        return self.x >= other.x and self.y >= other.y and self.z >= other.z

    def __le__(self, other):
        self.assertIfInvalid(other)

        return self.x <= other.x and self.y <= other.y and self.z <= other.z

    def __gt__(self, other):
        self.assertIfInvalid(other)

        return self.x > other.x and self.y > other.y and self.z > other.z

    def __lt__(self, other):
        self.assertIfInvalid(other)

        return self.x < other.x and self.y < other.y and self.z < other.z

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x + scalar, self.y + scalar, self.z + scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            vector = other
            return __class__(self.x + vector.x, self.y + vector.y, self.z + vector.z)

        assert False, "Invaild operand type: {}".format(type(other))

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x - scalar, self.y - scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            vector = other
            return __class__(self.x - vector.x, self.y - vector.y, self.z - vector.z)

        assert False, "Invaild operand type: {}".format(type(other))

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x * scalar, self.y * scalar, self.z * scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            vector = other
            return __class__(self.x * vector.x, self.y * vector.y, self.z * vector.z)

        assert False, "Invaild operand type: {}".format(type(other))

    def __pow__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x ** scalar, self.y ** scalar, self.z ** scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y'):
            vector = other
            return __class__(self.x ** vector.x, self.y ** vector.y, self.z ** vector.z)

        assert False, "Invaild operand type: {}".format(type(other))

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
