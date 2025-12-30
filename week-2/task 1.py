s = input().strip()

count = 0

for i in range(len(s-)):
    if s[i:i+5] == ">>-->" or s[i:i+5] == "<--<<":
        count += 1

print(count)
