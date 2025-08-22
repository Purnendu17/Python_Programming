s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]
result = new_s1 + " " + new_s2
print(result)