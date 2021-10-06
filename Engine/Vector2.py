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

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x + scalar, self.y + scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y'):
            vector = other
            return __class__(self.x + vector.x, self.y + vector.y)

        assert False, "Invaild Operand type."

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x - scalar, self.y - scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y'):
            vector = other
            return __class__(self.x - vector.x, self.y - vector.y)

        assert False, "Invaild Operand type."

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x * scalar, self.y * scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y'):
            vector = other
            return __class__(self.x * vector.x, self.y * vector.y)

        assert False, "Invaild Operand type."

    def __pow__(self, other):
        if type(other) == int or type(other) == float:
            scalar = other
            return __class__(self.x ** scalar, self.y ** scalar)
        elif hasattr(other, 'x') and hasattr(other, 'y'):
            vector = other
            return __class__(self.x ** vector.x, self.y ** vector.y)

        assert False, "Invaild Operand type."

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
