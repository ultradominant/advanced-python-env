import math

def triangle_area(a, h):
    return 0.5 * a * h

def hexagon_area(a):
    h = a * math.sqrt(3) / 2
    return 6 * triangle_area(a, h)

print("Hexagon area:", hexagon_area(5))

for i in range(3):
    a = float(input(f"Rectangle {i+1} side a: "))
    b = float(input(f"Rectangle {i+1} side b: "))
    print("Area:", a * b)
