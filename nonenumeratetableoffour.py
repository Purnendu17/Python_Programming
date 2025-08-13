def showtableof4():
    result = []
    for i in range(1, 21):
        result.append(i * 4)
    return result
result = showtableof4()
for i in range(1, 21):
    print("4 *", i, "=", result[i-1])