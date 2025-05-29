#multiplcation table of a give number

num = int(input('Multiplication table of(number):\n'))

print(f"Multiplication table of {num}\n")
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
