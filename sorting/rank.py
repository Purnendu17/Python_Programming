def selection_sort_desc(arr):
    n = len(arr)
    
    for i in range(n - 1):  # Sorting loop
        max_index = i  # Assume first unsorted element is the largest
        
        for j in range(i + 1, n):  # Find the index of the largest element
            if arr[j] > arr[max_index]:  
                max_index = j
        
        # Swap the found maximum element with the first element of unsorted part
        arr[i], arr[max_index] = arr[max_index], arr[i]

# Taking input from user
marks = []
for i in range(10):
    mark = int(input(f"Enter marks of student {i+1} (out of 100): "))
    marks.append(mark)

# Sorting marks in descending order
selection_sort_desc(marks)

# Display ranked marks
print("\nStudent Rankings (Highest to Lowest Marks):")
for rank, mark in enumerate(marks, start=1):
    print(f"Rank {rank}: {mark}")
