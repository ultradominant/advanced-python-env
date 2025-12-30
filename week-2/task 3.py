eq = input().strip()

if '+' in eq:
    parts = eq.split('+')
    a = parts[0]
    b_c = parts[1].split('=')
    b = b_c[0]
    c = b_c[1]
    op = '+'
else:
    parts = eq.split('-')
    a = parts[0]
    b_c = parts[1].split('=')
    b = b_c[0]
    c = b_c[1]
    op = '-'


if a != 'x':
    a = int(a)
if b != 'x':
    b = int(b)
if c != 'x':
    c = int(c)

if a == 'x':
    if op == '+':
        x = c - b
    else:
        x = c + b
elif b == 'x':
    if op == '+':
        x = c - a
    else:
        x = a - c
else:  # x == c
    if op == '+':
        x = a + b
    else:
        x = a - b

print(x)
