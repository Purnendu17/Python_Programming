num = int(input("Enter a number between 1 and 20: "))

# Check if the number is less than 2 or more than 20
if num < 2 or num > 20:
    print("Number out of range.")
else:
    # Check for primality
    if num == 2 or num == 3 or num == 5 or num == 7:
        print("prime")
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print("not prime")
    else:
        print("prime")
