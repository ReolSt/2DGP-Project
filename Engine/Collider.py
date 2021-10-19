from .Transform import *
from .GameObject import *
from .Ray import *

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

        assert isinstance(collider, Collider), "Invalid parameter type: {}".format(type(collider))

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

        assert isinstance(gameObject, GameObject), "Invalid parameter type: {}".format(type(gameObject))

        self.gameObject = gameObject
        self.transform = Transform(gameObject.transform)

        self.touchingColliders = []

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

    def isTouchingCollider(self, collider):
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

        return False

    def isTouchingRay(self, ray):
        """
        Parameters
        ----------
        ray : Ray
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """

        return False

    def isTouchingBox(self, left, right, bottom, top):
        """
        Parameters
        ----------
        left : int or float
            DESCRIPTION.
        right : int or float
            DESCRIPTION.
        bottom : int or float
            DESCRIPTION.
        top : int or float
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """

        return False

    def rayIntersectionPoint(self, ray):
        """
        Parameters
        ----------
        ray : Ray
            DESCRIPTION.

        Returns
        -------
        Vector2

        """

    def boxIntersectionPoint(self, ray, boxSize):
        """
        Parameters
        ----------
        ray : Ray
            DESCRIPTION.
        boxSize : Vector2
            DESCRIPTION.

        Returns
        -------
        Vector2

        """

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

    def render(self, camera):
        """

        Parameters
        ----------
        camera : Camera
            DESCRIPTION.

        Returns
        -------
        None.

        """
