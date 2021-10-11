class Vector2:
    def __init__(self, x=0.0, y=0.0):
        """
        Parameters
        ----------
        x : float, optional
            The default is 0.0.
        y : float, optional
            The default is 0.0.

        Returns
        -------
        None.

        """

        self.x = x
        self.y = y

    def copy(self):
        return __class__(self.x, self.y)

    def normalize(self):
        length = abs(self)
        return Vector2(self.x / length, self.y / length)

    def cross(self, other):
        if hasattr(other, 'x') and hasattr(other, 'y'):
            return self.x * other.y - self.y * other.x

        assert False, "Invalid operand type"

    def __eq__(self, other):
        assert hasattr(other, 'x') and hasattr(other, 'y'), "Invalid operand type"

        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        assert hasattr(other, 'x') and hasattr(other, 'y'), "Invalid operand type"

        return self.x != other.x or self.y != other.y

    def __ge__(self, other):
        assert hasattr(other, 'x') and hasattr(other, 'y'), "Invalid operand type"

        return self.x >= other.x and self.y >= other.y

    def __le__(self, other):
        assert hasattr(other, 'x') and hasattr(other, 'y'), "Invalid operand type"

        return self.x <= other.x and self.y <= other.y

    def __gt__(self, other):
        assert hasattr(other, 'x') and hasattr(other, 'y'), "Invalid operand type"

        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        assert hasattr(other, 'x') and hasattr(other, 'y'), "Invalid operand type"

        return self.x < other.x and self.y < other.y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x + scalar, self.y + scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y'):
            vector = other
            return __class__(self.x + vector.x, self.y + vector.y)

        assert False, "Invaild operand type."

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x - scalar, self.y - scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y'):
            vector = other
            return __class__(self.x - vector.x, self.y - vector.y)

        assert False, "Invaild operand type."

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x * scalar, self.y * scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y'):
            vector = other
            return __class__(self.x * vector.x, self.y * vector.y)

        assert False, "Invaild operand type."

    def __pow__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x ** scalar, self.y ** scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y'):
            vector = other
            return __class__(self.x ** vector.x, self.y ** vector.y)

        assert False, "Invaild operand type."

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
