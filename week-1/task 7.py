a = float(input("First number: "))
op = input("Operation: ")
b = float(input("Second number: "))

print("Error: division by zero") if op == "/" and b == 0 else print(
    a + b if op == "+" else
    a - b if op == "-" else
    a * b if op == "*" else
    a / b
)
