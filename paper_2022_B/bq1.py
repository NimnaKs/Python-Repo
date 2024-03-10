try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = num1 / num2
    print("A")
    # print("C")
except ZeroDivisionError as e:
    print("B")
else:
    print("C")
finally:
    print("D")
