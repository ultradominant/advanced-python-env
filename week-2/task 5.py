allowed_letters = set("ABCEHKMOPTXY")

n = int(input())

for _ in range(n):
    plate = input().strip()

    if len(plate) != 6:
        print("No")
        continue

    ok = True

    if plate[0] not in allowed_letters:
        ok = False
    if not plate[1:4].isdigit():
        ok = False
    if plate[4] not in allowed_letters or plate[5] not in allowed_letters:
        ok = False

    print("Yes" if ok else "No")
