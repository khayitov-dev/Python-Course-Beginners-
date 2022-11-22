### Calculator


num1 = float(input("Birinchi sonni kiriting: "))
op = input("Operator kiriting: ")
num2 = float(input("Ikkinchi sonni kiriting: "))


if op == '+':
    print("Javob:",num1 + num2)
elif op == '-':
    print("Javob:",num1 - num2)
elif op == '/':
    print("Javob:",num1 / num2)
elif op == '*':
    print("Javob:",num1 * num2)
else:
    print("Xato Operator!")
