from .Collider import *
from .Ray import *

class CollisionManager():
    def __init__(self):
        """
        Parameters
        ----------

        Returns
        -------
        None.

        """

        self.colliders = []

    def rayCast(self, origin, direction, distance, tag):
        """
        Parameters
        ----------
        origin : Vector2
            ray origin.
        direction : Vector2
            normalized direction vector.
        distance : float
            max distance from origin
        tag : str
            the collider tag that want to hit ray

        Returns
        -------
        None.

        """

        assert isinstance(origin, Vector2), "rayCast : origin is not Vector2"
        assert isinstance(direction, Vector2), "rayCast : direction is not Vector2"

        ray = Ray(origin, direction, distance)

        for collider in self.colliders:
            if collider.tag == tag and collider.isTouchingRay(ray):
                hitPoint = collider.rayIntersectionPoint(ray)
                return RayCastHit(collider, origin, direction, abs(hitPoint - origin), hitPoint, tag)

        return None

    def boxCast(self, origin, size, direction, distance, tag):
        """
        Parameters
        ----------
        origin : Vector2
            ray origin
        size : Vector2
            box size
        direction : Vector2
            normalized direction vector.
        distance : float
            max distance from origin
        tag : str
            the collider tag that want to hit ray

        Returns
        -------
        TYPE
            DESCRIPTION.

        """


        assert isinstance(origin, Vector2), "boxCast : origin is not Vector2"
        assert isinstance(direction, Vector2), "boxCast : direction is not Vector2"



    def update(self):
        """
        Returns
        -------
        None.

        """

        for i in range(len(self.colliders)):
            for j in range(i + 1, len(self.colliders)):
                colliderA = self.colliders[i]
                colliderB = self.colliders[j]

                directionA = colliderA.relativeDirection(colliderB)
                directionB = colliderB.relativeDirection(colliderA)

                objectA = colliderA.gameObject
                objectB = colliderB.gameObject

                if colliderA.isTouchingCollider(colliderB):
                    if colliderB not in colliderA.touchingColliders:
                        objectA.onCollisionEnter(Collision(colliderB, directionA))
                        colliderA.touchingColliders.append(colliderB)
                    if colliderA not in colliderB.touchingColliders:
                        direction = colliderA.relativeDirection
                        objectB.onCollisionEnter(Collision(colliderA, directionB))
                        colliderB.touchingColliders.append(colliderA)

                    objectA.onCollisionStay(Collision(colliderB, directionA))
                    objectB.onCollisionStay(Collision(colliderA, directionB))
                else:
                    if colliderB in colliderA.touchingColliders:
                        colliderA.touchingColliders.remove(colliderB)
                        objectA.onCollisionExit(Collision(colliderB, directionA))
                    if colliderA in colliderB.touchingColliders:
                        colliderB.touchingColliders.remove(colliderA)
                        objectB.onCollisionExit(Collision(colliderA, directionB))


    def addCollider(self, collider):
        """
        Parameters
        ----------
        gameObject : GameObject
            DESCRIPTION.

        Returns
        -------
        None.

        """

        assert isinstance(collider, Collider), "invalid parameter type: {}".format(type(collider))

        self.colliders.append(collider)

    def removeCollider(self, colliderToRemove):
        """
        Parameters
        ----------
        collider : ColliderToRemove
            DESCRIPTION.

        Returns
        -------
        None.

        """

        assert isinstance(colliderToRemove, Collider), "invalid parameter type: {}".format(type(collider))

        if colliderToRemove in self.colliders:
            self.colliders.remove(colliderToRemove)

        for collider in self.colliders:
            if colliderToRemove in collider.touchingColliders:
                collider.touchingColliders.remove(colliderToRemove)