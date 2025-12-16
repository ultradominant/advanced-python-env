ticket = input()

first = sum(map(int, ticket[:3]))
last = sum(map(int, ticket[3:]))

print("YES" if first == last else "NO")
