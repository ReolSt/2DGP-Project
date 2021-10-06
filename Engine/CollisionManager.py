from .Collider import *

class CollisionManager():
    def __init__(self, scene):
        """
        Parameters
        ----------
        scene : Scene
            DESCRIPTION.

        Returns
        -------
        None.

        """

        self.scene = scene
        self.objects = []

    def rayCast(self, origin, direction, distance, tag):
        """
        Parameters
        ----------
        origin : Vector2
            ray origin.
        direction : Vector2
            normalized direction vector.
        distance : float
            DESCRIPTION.
        tag : str
            DESCRIPTION.

        Returns
        -------
        None.

        """
        pass

    def boxCast(self, origin, size, direction, distance, tag):
        pass

    def Update(self):
        """
        Returns
        -------
        None.

        """

        for i in range(len(self.objects)):
            for j in range(i + 1, len(self.objects)):
                objectA = self.objects[i]
                objectB = self.objects[j]

                colliderA = objectA.collider
                colliderB = objectB.collider

                directionA = colliderA.relativeDirection(colliderB)
                directionB = colliderB.relativeDirection(colliderA)

                if colliderA.isTouching(colliderB):
                    if objectB.id not in colliderA.touchingObjects:
                        objectA.onCollisionEnter(Collision(colliderB, directionA))
                        colliderA.touchingObjects[objectB.id] = objectB
                    if objectA.id not in colliderB.touchingObjects:
                        direction = colliderA.relativeDirection
                        objectB.onCollisionEnter(Collision(colliderA, directionB))
                        colliderB.touchingObjects[objectA.id] = objectA

                    objectA.onCollisionStay(Collision(colliderB, directionA))
                    objectB.onCollisionStay(Collision(colliderA, directionB))
                else:
                    if objectB.id in colliderA.touchingObjects:
                        colliderA.touchingObjects.pop(objectB.id)
                        objectA.onCollisionExit(Collision(colliderB, directionA))
                    if objectA.id in colliderB.touchingObjects:
                        colliderB.touchingObjects.pop(objectA.id)
                        objectB.onCollisionExit(Collision(colliderA, directionB))


    def addObject(self, gameObject):
        """
        Parameters
        ----------
        gameObject : GameObject
            DESCRIPTION.

        Returns
        -------
        None.

        """

        assert(hasattr(gameObject, "collider") and isinstance(gameObject.collider, Collider))

        self.objects.append(gameObject)

    def removeObject(self, idOrGameObject):
        """
        Parameters
        ----------
        idOrGameObject : int or GameObject
            DESCRIPTION.

        Returns
        -------
        None.

        """

        assert(isinstance(idOrGameObject, int) or isinstance(idOrGameObject, GameObject))

        if isinstance(idOrGameObject, GameObject):
            gameObject = idOrGameObject
            if gameObject in self.objects:
                self.objects.remove(gameObject)

            for collisionObject in self.objects:
                collider = collisionObject.collider
                if gameObject.id in collider.touchingObjects:
                    collider.touchingObject.pop(gameObject.id)
        else:
            objectId = idOrObject
            for i in range(len(self.objects)):
                if self.objects[i].id == objectId:
                    self.objects.pop(i)

            for collisionObject in self.objects:
                collider = collisionObject.collider
                if objectId in collider.touchingObjects:
                    collider.touchingObject.pop(objectId)