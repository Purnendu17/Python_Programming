a = int(input("How many numbers do you wish to input: "))
total_sum = 0  
for i in range(a):
    b = int(input("Enter number {i + 1}: ")) 
    total_sum += b  
average = total_sum / a
print("Average =", average)