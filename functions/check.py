def check_for_five(numbers):
    indices = []
    for index, number in enumerate(numbers):
        if number == 5:
            indices.append(index)
    if indices:
        for idx in indices:
            print("5 is present at index", {idx})
    else:
        print("5 is not present in the list.")

    contains_five = False
    for index, number in enumerate(numbers):
        if '5' in str(number):
            print("The number",{number}, "at index", {index}, "contains '5'.")
            contains_five = True

    if not contains_five:
        print("There are no numbers in the list that contain '5'.")

numbers = [25, 55, 888, 127, 34, 15]
check_for_five(numbers)


