s = input("Enter a string: ")
if len(s) < 2:
    result = ""
else:
    result = s[:2] + s[-2:]
print(result)