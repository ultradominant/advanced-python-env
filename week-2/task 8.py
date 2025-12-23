s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("NO")
else:
    if sorted(s1) == sorted(s2):
        print("YES")
    else:
        print("NO")
