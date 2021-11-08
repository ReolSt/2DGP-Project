import pymunk
import os
import pico2d

if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Transform import *
else:
    from .Transform import *

class RigidBody:
    static = pymunk.Body.STATIC
    kinematic = pymunk.Body.KINEMATIC
    dynamic = pymunk.Body.DYNAMIC

    def __init__(self, gameObject, body, shape):
        self.gameObject = gameObject

        self.body : pymunk.Body = body
        self.shape : pymunk.Poly = shape

        self.vertices = shape.get_vertices()
        self.scale = gameObject.transform.getScale()

    @property
    def bodyType(self):
        return self.body.body_type

    @bodyType.setter
    def bodyType(self, bodyType):
        if isinstance(bodyType, str):
            if bodyType in ["STATIC", "Static", "static"]:
                bodyType = RigidBody.static
            elif bodyType in ["KINEMATIC", "Static", "static"]:
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

    def sync(self):
        if self.body.body_type == self.body.DYNAMIC:
            position = self.body.position
       
            self.gameObject.transform.setPosition(position.x, position.y)

    def update(self):
        position = self.gameObject.transform.getPosition()
        scale = self.gameObject.transform.getScale()

        self.body.position = position.x, position.y

        if scale != self.scale:
            space = self.body.space
            space.remove(self.body, self.shape)

            scaleTransform = pymunk.Transform(a=scale.x, b=0, c=0, d=scale.y, tx=0, ty=0)

            self.shape = pymunk.Poly(self.body, self.vertices, scaleTransform)
            self.scale = scale.copy()
            
            self.vertices = self.shape.get_vertices()

            space.add(self.body, self.shape)

    def render(self, camera):
        position = camera.translate(Vector2(self.body.position.x, self.body.position.y))
        scale = camera.scale(Vector2(1.0, 1.0))

        bb = self.shape.bb;

        leftBottom = camera.translate(Vector2(bb.left, bb.bottom)) * scale
        rightTop = camera.translate(Vector2(bb.right, bb.top)) * scale

        pico2d.draw_rectangle(leftBottom.x, leftBottom.y, rightTop.x, rightTop.y)