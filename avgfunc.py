def find_average():
    count = int(input("How many numbers do you want to enter? "))
    total = 0
    for i in range(count):
        num = float(input(f"Enter number {i+1}: "))
        total += num  
    if count > 0:
        average = total / count
        print(f"The average is: {average}")
    else:
        print("No numbers entered to calculate average.")
find_average()
