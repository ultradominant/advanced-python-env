items = input().split()

counts = {}

for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print("Purchase frequency:")
for item in counts:
    print(item + ":", counts[item])

most_popular = max(counts, key=counts.get)
print("Most popular item:", most_popular)

once = []
for item in counts:
    if counts[item] == 1:
        once.append(item)

print("Purchased once:", " ".join(once))

sorted_items = sorted(counts.items(), key=lambda x: -x[1])

print("Sorted by frequency:")
for item, cnt in sorted_items:
    print(item, cnt)
