number = int(input("Enter number:"))
binary_representation = ""

if number == 0:
    binary_representation = "0"

while number > 0:
    remainder = number % 2  
    binary_representation = str(remainder) + binary_representation 
    number = number // 2  

print(f"The binary representation is",binary_representation)