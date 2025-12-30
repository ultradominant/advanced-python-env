def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def subtract_fractions(a, b, c, d):
    num = a * d - b * c
    den = b * d
    g = gcd(abs(num), den)
    return num // g, den // g

print("Subtraction:", subtract_fractions(3, 4, 1, 2))

n = int(input("Enter number: "))
divs = [str(i) for i in range(1, n+1) if n % i == 0]
print("Divisors:", " ".join(divs))
