numbers = [13, 19, 26, 38, 39, 57, 76, 95, 100, 247]
divisible = list(filter(lambda x: x % 13 == 0 or x % 19 == 0, numbers))
print(f"Numbers divisible by 13 or 19: {divisible}")
