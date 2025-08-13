a = [1, 2, 3, 4, 5]
i = 0
while i < 4:  
    adjacent_sum = a[i] + a[i + 1]
    print("Sum of", a[i], "and", a[i + 1], ":", adjacent_sum)
    i += 1 