def sum(x, y):
    return x + y
def subtract(x, y):
    return x - y
print("Simple Calculator")
print("18. Add")
print("36. Subtract")
choice = input("Enter 18 or 36: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '18':
    print("Result:", add(num1, num2))
elif choice == '36':
    print("Result:", subtract(num1, num2))
else:
    print("Invalid choice")
