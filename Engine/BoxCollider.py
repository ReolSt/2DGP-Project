from .Transform import *
from .Collider import *

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
    def __init__(self, gameObject, width=1, height=1):
        """
        Parameters
        ----------
        gameObject : GameObject
            DESCRIPTION.
        width : int or float, optional
            DESCRIPTION. The default is 1.
        height : int or float, optional
            DESCRIPTION. The default is 1.

        Returns
        -------
        None.

        """

        super().__init__(gameObject)

        self.width = width
        self.height = height

    def getAABB():
        """
        Returns
        -------
        AABB
            DESCRIPTION.

        """

        position = self.transform.position()

        left = position[0] - self.width / 2
        right = position[0] + self.width / 2
        bottom = position - self.height / 2
        top = position[0] + self.height / 2

        return AABB(left, right, bottom, top)


    def isTouching(collider):
        """
        Parameters
        ----------
        collider : Collider
            DESCRIPTION.

        Returns
        -------
        bool

        """

        assert(isinstance(collider, Collider))

        if isinstance(collider, BoxCollider):
            aabb = self.getAABB()
            colliderAABB = collider.getAABB()

            if aabb.right < colliderAABB.left:
                return False
            if aabb.left > colliderAABB.right:
                return False
            if aabb.top < colliderAABB.bottom:
                return False
            if aabb.bottom > colliderAABB.top:
                return False

        return True
