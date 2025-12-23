eq = input().strip()

a = eq[0]
op = eq[1]
b = eq[2]
c = eq[4]

if a == 'x':
    b = int(b)
    c = int(c)
    if op == '+':
        x = c - b
    else:
        x = c + b

elif b == 'x':
    a = int(a)
    c = int(c)
    if op == '+':
        x = c - a
    else:
        x = a - c

else:
    a = int(a)
    b = int(b)
    if op == '+':
        x = a + b
    else:
        x = a - b

print(x)
