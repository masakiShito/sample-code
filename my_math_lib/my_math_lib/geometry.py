import math

def circle_area(radius):
    if radius < 0:
        raise ValueError("半径は0以上でなければなりません")
    return math.pi * radius ** 2

def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("長さと幅は0以上でなければなりません")
    return length * width
