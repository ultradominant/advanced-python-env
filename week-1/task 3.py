a = float(input())

integer_part = int(a)
fractional_part = int((a - integer_part) * 100)

new_number = fractional_part + integer_part / 100
print(new_number)
