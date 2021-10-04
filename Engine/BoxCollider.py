from .Transform import *

class Collision:
    def __init__(self):
        pass

class Collider:
    def __init__(self, gameObject):
        self.gameObject = gameObject
        self.transform = Transform(gameObject)

    def isTouching(collider):
        assert(isinstance(collider, Collider))

        return False

class AABB:
    def __init__(self, left, right, bottom, top):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top

class BoxCollider:
    def __init__(self, gameObject, width=1, height=1):
        super().__init__(gameObject)

        self.width = width
        self.height = height

    def getAABB():
        position = self.transform.position()
        scale = self.transform.scale()

        width = self.width * scale[0]
        height = self.height * scale[1]

        left = position[0] - width / 2
        right = position[0] + width / 2
        bottom = position - height / 2
        top = position[0] + height / 2

        return AABB(left, right, bottom, top)


    def isTouching(collider):
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
