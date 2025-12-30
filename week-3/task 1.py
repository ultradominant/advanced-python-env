import math

def circle_area(r):
    return math.pi * r * r

def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return 0.5 * a * h

arrays = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [10, 20]
]

for arr in arrays:
    s = sum(arr)
    mean = s / len(arr)
    print(f"Array: {arr}, Sum: {s}, Mean: {mean}")
