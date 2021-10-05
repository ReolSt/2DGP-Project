from .Transform import *

class Collision:
    def __init__(self, collider, direction):
        """
        Parameters
        ----------
        collider : Collider
            DESCRIPTION.
        direction : list of float
            Relative Direction Vector, contains x and y of 2d vector

        Returns
        -------
        None.

        """

        assert(isinstance(collider, Collider))

        self.gameObject = collider.gameObject
        self.direction = direction

class Collider:
    def __init__(self, gameObject):
        """
        Parameters
        ----------
        gameObject : GameObject
            Game object to attach itself.

        Returns
        -------
        None.


        """

        self.gameObject = gameObject
        self.transform = Transform(gameObject)

        self.touchingObjects = {}

    def getGroup(self):
        """
        Returns
        -------
        str

        """

        return self.group

    def setGroup(self, group):
        """
        Parameters
        ----------
        group : str
            The group name.

        Returns
        -------
        None

        """

        self.group = group

    def isTouching(self, collider):
        """
        Parameters
        ----------
        collider : Collider
            The collider to check.

        Returns
        -------
        bool
            DESCRIPTION.

        """

        assert(isinstance(collider, Collider))

        return False

    def relativeDirection(self, collider):
        """
        Parameters
        ----------
        collider : Collider
            DESCRIPTION.

        Returns
        -------
        list of float
            Contains x and y of 2d vector

        """

        position = self.transform.position()

        x, y = position[0], position[1]

        colliderPosition = collider.transform.position()
        cx, cy = colliderPosition[0], colliderPosition[1]

        rx = cx - x
        ry = cy - y

        magnitude = (rx ** 2 + ry ** 2) ** 0.5
        if magnitude == 0.0:
            return [0.0, 0.0]

        return [rx / magnitude, ry / magnitude]
