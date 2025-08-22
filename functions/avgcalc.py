def calculate_average(args):
    if args==0: 
        return "No data"
    return sum(args) / len(args)

num_args = int(input("Enter the number of arguments: "))
if num_args == 0:
        print("No data")
else:
        arguments = []
        for i in range(num_args):
            value = int(input(f"Enter value {i + 1}: "))  
            arguments.append(value)
        average = calculate_average(arguments)
        print("The average is:", {average})

