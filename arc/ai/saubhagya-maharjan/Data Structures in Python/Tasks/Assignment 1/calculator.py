a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
print("Choose the operation:")
print('1. Add')
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponential")
print("6. Floor Division")
print("7. Modulo Operator")

operation = input("Chose the number:")

if operation == '1':
    print(f"Result: {a + b}")
elif operation == '2':
    print(f"Result: {a - b}")
elif operation == '3':
    print(f"Result: {a * b}")
elif operation == '4':
    if b == 0:
        print("Error:Divisible by 0 is not possible.")
    else:
         print(f"Result: {a / b}")
elif operation == '5':
    print(f"Result: {a ** b}")
elif operation == '6':
    print(f"Result: {a // b}")
elif operation == '7':
    if b == 0:
        print("Error:Module by 0 is not possible.")
    else:
        print(f"Result: {a % b}")
else:
    print('Input invalid.')        

