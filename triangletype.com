import math

def triangle_type(a, b, c):
    a, b, c = float(a), float(b), float(c)
    angles = []
    angle_str = 'math.acos(({0}**2 + {1}**2 - {2}**2)/(2*{0}*{1}))'
    try:
        angles.append(math.degrees(eval(angle_str.format(b,c,a))))
        angles.append(math.degrees(eval(angle_str.format(c,a,b))))
        angles.append(math.degrees(eval(angle_str.format(a,b,c))))
    except ValueError as e:
        return 0
    if sum(angles) == 180 and max(angles) < 180: 
        if 90 in angles:
            return 2
        return 3 if max(angles) > 90 else 1
    else:
        return 0

if __name__=='__main__':
    print(triangle_type(7,3,2))
    print(triangle_type(2,4,6))
    print(triangle_type(8,5,7))
    print(triangle_type(3,4,5))
    print(triangle_type(7,12,8))
