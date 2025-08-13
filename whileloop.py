num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
while num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder
print("The HCF is:", num1)