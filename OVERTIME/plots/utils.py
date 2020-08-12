
import math



def vector_angle(x, y):
    hypot = math.sqrt(x*x + y*y)
    theta = math.asin(y / hypot)
    if x < 0:
        theta = math.pi - theta
    if theta < 0:
        theta = theta + 2*math.pi
    return theta


def circle_label_angle(x, y):
    angle = math.degrees(vector_angle(x, y))
    if angle > 90 and angle < 270:
        return angle - 180
    else:
        return angle


def bezier(p1, p2, p0=(0,0), nt=20):
    bezier = {}
    bezier['x'] = []
    bezier['y'] = []
    for i in range(0, nt+1):
        t = (1/nt) * i
        bezier['x'].append(
            (p1['x']-2*p0[0]+p2['x'])*math.pow(t,2) + 2*t*(p0[0]-p1['x']) + p1['x']
        )
        bezier['y'].append(
            (p1['y']-2*p0[0]+p2['y'])*math.pow(t,2) + 2*t*(p0[0]-p1['y']) + p1['y']
        )
    return bezier
