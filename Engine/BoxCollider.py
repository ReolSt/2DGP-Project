from .Transform import *
from .Collider import *
from .Math import *

class AABB:
    def __init__(self, left, right, bottom, top):
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
        None.

        """

        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top

class BoxCollider(Collider):
    def __init__(self, gameObject, width, height):
        """
        Parameters
        ----------
        gameObject : GameObject
            DESCRIPTION.
        width : int or float
            DESCRIPTION.
        height : int or float
            DESCRIPTION.

        Returns
        -------
        None.

        """

        super().__init__(gameObject)

        self.width = width
        self.height = height

    def aabb(self):
        """
        Returns
        -------
        AABB
            DESCRIPTION.

        """

        position = self.transform.position()
        scale = self.transform.scale()

        width = self.width * scale.x
        height = self.height * scale.y


        left = position.x - width / 2
        right = position.x + width / 2
        bottom = position.y - height / 2
        top = position.y + height / 2

        return AABB(left, right, bottom, top)


    def isTouchingCollider(self, collider):
        """
        Parameters
        ----------
        collider : Collider
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """

        assert isinstance(collider, Collider), "isTouchingCollider : invalid parameter."

        aabb = self.aabb()

        if isinstance(collider, BoxCollider):
            colliderAABB = collider.aabb()

            return self.isTouchingBox(
                colliderAABB.left,
                colliderAABB.right,
                colliderAABB.bottom,
                colliderAABB.top)

        return True

    def rayIntersectionPoint(self, ray):
        """
        Parameters
        ----------
        ray : Ray
            DESCRIPTION.

        Returns
        -------
        None.

        """

        aabb = self.aabb()

        rayStart = ray.origin
        rayEnd = ray.origin + ray.direction * ray.distance

        leftBottom = Vector2(aabb.left, aabb.bottom)
        leftTop = Vector2(aabb.left, aabb.top)
        rightBottom = Vector2(aabb.right, aabb.bottom)
        rightTop = Vector2(aabb.right, aabb.top)

        minDistancePoint = None
        minDistance = None

        edges = [
            (leftBottom, leftTop),
            (rightBottom, rightTop),
            (leftBottom, rightBottom),
            (leftTop, rightTop)
        ]

        for p1, p2 in edges:
            point = getIntersectionPoint(rayStart, rayEnd, p1, p2)
            distance = abs(point - ray.origin)
            if minDistancePoint is None or minDistance > distance:
                minDistancePoint = point
                minDistance = distance

        return minDistancePoint

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

        assert isinstance(ray, Ray), "Invalid parameter type: {}".format(type(ray))

        aabb = self.aabb()

        rayStart = ray.origin
        rayEnd = ray.origin + ray.direction * ray.distance

        leftBottom = Vector2(aabb.left, aabb.bottom)
        leftTop = Vector2(aabb.left, aabb.top)
        rightBottom = Vector2(aabb.right, aabb.bottom)
        rightTop = Vector2(aabb.right, aabb.top)

        result = False

        edges = [
            (leftBottom, leftTop),
            (rightBottom, rightTop),
            (leftBottom, rightBottom),
            (leftTop, rightTop)
        ]

        for p1, p2 in edges:
            result |= isIntersecting(rayStart, rayEnd, p1, p2)

        return result

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

        aabb = self.aabb()

        if aabb.right < left:
            return False
        if aabb.left > right:
            return False
        if aabb.top < bottom:
            return False
        if aabb.bottom > top:
            return False

        return True