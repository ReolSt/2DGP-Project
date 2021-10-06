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

        self.collider = collider
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

        self.tag = ""

    def getTag(self):
        """
        Returns
        -------
        str

        """

        return self.tag

    def setTag(self, tag):
        """
        Parameters
        ----------
        tag : str
            The tag name.

        Returns
        -------
        None

        """

        self.tag = tag

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

        x, y = position.x, position.y

        colliderPosition = collider.transform.position()
        cx, cy = colliderPosition.x, colliderPosition.y

        rx = cx - x
        ry = cy - y

        magnitude = (rx ** 2 + ry ** 2) ** 0.5
        if magnitude == 0.0:
            return [0.0, 0.0]

        return [rx / magnitude, ry / magnitude]
