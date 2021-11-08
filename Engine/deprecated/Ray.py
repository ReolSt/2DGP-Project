from Engine.Vector2 import *

class Ray:
    def __init__(self, origin, direction, distance):
        """
        Parameters
        ----------
        origin : Vector2
            DESCRIPTION.
        direction : Vector2
            DESCRIPTION.
        distance : float
            DESCRIPTION.

        Returns
        -------
        None.

        """

        self.origin = origin
        self.direction = direction
        self.distance = distance

class RayCastHit:
    def __init__(self, collider, origin, direction, distance, hitPoint, tag):
        """
        Parameters
        ----------
        collider : Collider
            DESCRIPTION.
        origin : Vector2
            DESCRIPTION.
        direction : Vector2
            DESCRIPTION.
        distance : float
            DESCRIPTION.
        hitPoint : Vector2
            DESCRIPTION.
        tag : str
            DESCRIPTION.

        Returns
        -------
        None.

        """

        self.collider = collider
        self.origin = origin
        self.direction = direction
        self.distance = distance
        self.hitPoint = hitPoint
        self.tag = tag