def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print("GCD:", gcd(12, 18))
print("LCM:", lcm(12, 18))

import math

def quad_area(a, b, c, d, diag):
    s1 = (a + b + diag) / 2
    s2 = (c + d + diag) / 2
    area1 = math.sqrt(s1*(s1-a)*(s1-b)*(s1-diag))
    area2 = math.sqrt(s2*(s2-c)*(s2-d)*(s2-diag))
    return area1 + area2

print("Quadrilateral area:", quad_area(3,4,5,6,7))
