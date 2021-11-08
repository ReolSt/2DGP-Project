import os

if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from Vector2 import *
    from Vector3 import *
else:
    from .Vector2 import *
    from .Vector3 import *

def ccw(p1, p2, p3):
    """
    Parameters
    ----------
    p1 : Vector2
        DESCRIPTION.
    p2 : Vector2
        DESCRIPTION.
    p3 : Vector2
        DESCRIPTION.

    Returns
    -------
    float
        counterclockwise if greater than 0
        parallel if equal to 0
        clockwise if less than 0

    """

    return p1.x * p2.y + p2.x * p3.y + p3.x * p1.y \
        - p1.y * p2.x - p2.y * p3.x - p3.y * p1.x

def isIntersecting(p1, p2, p3, p4):
    """
    Parameters
    ----------
    p1 : Vector2
        the first point of first edge
    p2 : Vector2
        the second point of first edge
    p3 : Vector2
        the first point of first edge
    p4 : Vector2
        the second point of first edge

    Returns
    -------
    bool

    """

    a = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    b = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    if a == 0 and b == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3

        return p3 <= p2 and p1 <= p4

    return a <= 0 and b <= 0


def getIntersectionPoint(p1, p2, p3, p4):
    """
    Parameters
    ----------
    p1 : Vector2
        the first point of first edge
    p2 : Vector2
        the second point of first edge
    p3 : Vector2
        the first point of first edge
    p4 : Vector2
        the second point of first edge

    Returns
    -------
    Vector2

    """

    p1 = Vector3(p1.x, p1.y, 1)
    p2 = Vector3(p2.x, p2.y, 1)
    p3 = Vector3(p3.x, p3.y, 1)
    p4 = Vector3(p4.x, p4.y, 1)

    v = p1.cross(p2).cross(p3.cross(p4))

    if v.z == 0.0:
        return Vector2(float('inf'), float('inf'))

    return Vector2(v.x / v.z, v.y / v.z)