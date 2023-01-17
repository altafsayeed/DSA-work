num1 = 11
num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1)) # id() gives address of where something is stored
print("num2 points to:", id(num2))