def right_triangle_area(a, b):
    return a * b / 2

def rectangle_area(a, b):
    return a * b

x, y, z, t = 3, 4, 5, 6
area = right_triangle_area(x, y) + rectangle_area(z, t)
print("Area:", area)

n = int(input("Enter number: "))
print(format(n, "010o"))
