
import math



def vector_angle(x, y):
    hypot = math.sqrt(x*x + y*y)
    theta = math.asin(y / hypot)
    if x < 0:
        theta = math.pi - theta
    if theta < 0:
        theta = theta + 2*math.pi
    return theta
