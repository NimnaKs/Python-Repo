num = int(input("Enter factorial number :"))
factorial = 1
for a in range(0, num + 1):
    if a == 0:
        factorial *= 1
        # factorial = factorial * 1
        # factorial =  1 * 1
    else:
        factorial *= a
        # factorial = 1 * 2
        # 2 * 3
        # 6 * 4
        # 24 * 5

print(f"The factorial of {num} is : = {factorial}")
