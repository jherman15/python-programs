# from klasy import liczby_zespolone
# OR
from klasy.liczby_zespolone import ComplexNumber

# num1 = ComplexNumber(input("Enter first number: "))
# num2 = ComplexNumber(input("Enter second number: "))

num1 = ComplexNumber(3, 15j)
num2 = ComplexNumber(1, 12j)

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice: 1, 2, 3, or 4: ")

if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '/4':
    result = num1 / num2
else:
    raise RuntimeError("Invalid input")

# print(f"The result is {result}")


