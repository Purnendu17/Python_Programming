def showtableof4():
    result = []
    for i in range(1, 21):
        result.append(i * 4)
    return result
for i, value in enumerate(showtableof4(), start=1):
    print("4 *", i, "=", value)