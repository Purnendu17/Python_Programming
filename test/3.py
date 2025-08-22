s = input("Enter a string: ")
n = int(input("Enter the position of the character to remove (starting from 0): "))
result = s[:n] + s[n+1:]
print(result)