import pymunk
import os
import pico2d

if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Transform import Transform
    from Vector2 import Vector2
else:
    from .Transform import Transform
    from .Vector2 import Vector2

class RigidBody:
    static = pymunk.Body.STATIC
    kinematic = pymunk.Body.KINEMATIC
    dynamic = pymunk.Body.DYNAMIC

    def __init__(self, gameObject, body=None, shape=None):
        self.gameObject = gameObject

        self.__body : pymunk.Body = body if body is not None else pymunk.Body()
        self.__shape : pymunk.Poly = shape if shape is not None else pymunk.Poly(self.__body, [])

        self.__vertices = self.__shape.get_vertices()
        self.__scale = self.gameObject.transform.getScale()

    @property
    def space(self):
        return self.__body.space

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        assert isinstance(body, pymunk.Body), "[RigidBody] body.setter : Invalid parameter. ( {} )".format(body)
        space = self.__body.space
        space.remove(self.__body, self.__shape)
        self.__body = body
        space.add(self.__body, self.__shape)

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape):
        assert isinstance(shape, pymunk.Shape), "[RigidBody] shape.setter : Invalid parameter. ( {} )".format(shape)
        space = self.__body.space

        space.remove(self.__body, self.__shape)
        self.__shape = shape
        space.add(self.__body, self.__shape)

        self.__vertices = self.shape.get_vertices()

    @property
    def bodyType(self):
        return self.body.body_type

    @bodyType.setter
    def bodyType(self, bodyType):
        if isinstance(bodyType, str):
            if bodyType in ["STATIC", "Static", "static"]:
                bodyType = RigidBody.static
            elif bodyType in ["KINEMATIC", "Kinematic", "kinematic"]:
                bodyType = RigidBody.kinematic
            elif bodyType in ["DYNAMIC", "Dynamic", "dynamic"]:
                bodyType = RigidBody.dynamic
            else:
                assert False, "[RigidBody] bodyType.setter : Invalid parameter ( bodyType = {} )".format(bodyType)

        self.body.body_type = bodyType

    @property
    def filter(self):
        return self.shape.filter

    @filter.setter
    def filter(self, filter):
        if isinstance(filter, int):
            self.shape.filter = pymunk.ShapeFilter(categories=filter)
        else:
            self.shape.filter = filter

    @property
    def angle(self):
        return self.body.angle

    @angle.setter
    def angle(self, angle):
        self.body.angle = angle

    @property
    def velocity(self):
        return self.body.velocity

    @velocity.setter
    def velocity(self, velocity):
        self.body.velocity = velocity

    @property
    def velocityX(self):
        return self.body.velocity.x

    @velocityX.setter
    def velocityX(self, x):
        self.body.velocity = x, self.body.velocity.y

    @property
    def velocityY(self):
        return self.body.velocity.y

    @velocityY.setter
    def velocityY(self, y):
        self.body.velocity = self.body.velocity.x, y

    @property
    def torque(self):
        return self.body.torque

    @torque.setter
    def torque(self, torque):
        self.body.torque = torque

    @property
    def mass(self):
        return self.body.mass

    @mass.setter
    def mass(self, mass):
        self.body.mass = mass

    @property
    def moment(self):
        return self.body.moment

    @moment.setter
    def moment(self, moment):
        self.body.moment = moment

    @property
    def elasticity(self):
        return self.shape.elasticity

    @elasticity.setter
    def elasticity(self, elasticity):
        self.shape.elasticity = elasticity

    @property
    def friction(self):
        return self.shape.friction

    @friction.setter
    def friction(self, friction):
        self.shape.friction = friction

    @property
    def vertices(self):
        return self.shape.get_vertices()

    @vertices.setter
    def vertices(self, vertices):
        shape = pymunk.Poly(self.body, vertices)

        shape.filter = self.filter
        shape.elasticity = self.elasticity
        shape.friction = self.friction

        self.shape = shape

    @property
    def bb(self):
        return self.shape.bb

    def sync(self):
        position = self.body.position
        self.gameObject.transform.setPosition(position.x, position.y)

    def update(self):
        position = self.gameObject.transform.getPosition()
        scale = self.gameObject.transform.getScale()

        self.body.position = position.x, position.y

        if scale != self.__scale:
            filter = self.filter
            elasticity = self.elasticity
            friction = self.friction

            space = self.__body.space
            space.remove(self.__body, self.__shape)

            scaleTransform = pymunk.Transform(a=scale.x, b=0, c=0, d=scale.y, tx=0, ty=0)

            self.__shape = pymunk.Poly(self.__body, self.__vertices, scaleTransform)
            self.__scale = scale.copy()

            self.__vertices = self.__shape.get_vertices()

            space.add(self.__body, self.__shape)

            self.filter = filter
            self.elasticity = elasticity
            self.friction = friction

    def render(self, camera):
        position = camera.translate(Vector2(self.body.position.x, self.body.position.y))
        scale = camera.scale(Vector2(1.0, 1.0))

        bb = self.shape.bb;

        leftBottom = camera.translate(Vector2(bb.left, bb.bottom)) * scale
        rightTop = camera.translate(Vector2(bb.right, bb.top)) * scale

        pico2d.draw_rectangle(leftBottom.x, leftBottom.y, rightTop.x, rightTop.y)