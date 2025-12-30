def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def divide_fractions(a, b, c, d):
    num = a * d
    den = b * c
    g = gcd(num, den)
    return num // g, den // g

print("Division:", divide_fractions(1, 2, 3, 4))

def inside_circle(x, y, a, b, r):
    return (x - a)**2 + (y - b)**2 < r*r

points = [(1, 2), (3, 4), (0, 0)]
count = 0

for p in points:
    if inside_circle(p[0], p[1], 0, 0, 5):
        count += 1

print("Points inside circle:", count)
