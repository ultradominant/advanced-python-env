n = int(input("Enter n: "))

for i in range(1, n+1):
    digits = [int(d) for d in str(i) if d != '0']
    if digits and all(i % d == 0 for d in digits):
        print(i, end=" ")
print()

def swap_first_last(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input("Array length: "))
A = list(map(int, input("Enter elements: ").split()))

print("Original:", A)
swap_first_last(A)
print("Result:", A)
