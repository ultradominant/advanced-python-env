a = input().strip()
b = input().strip()

b_len = len(b)
count = 0

shifts = []
for i in range(len(b)):
    shifts.append(b[i:] + b[:i])

for i in range(len(a) - b_len + 1):
    sub = a[i:i+b_len]
    if sub in shifts:
        count += 1

print(count)
