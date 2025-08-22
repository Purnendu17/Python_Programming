def heapify_max(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_max(arr, n, largest)

def heap_sort_ascending(arr):
    n = len(arr)

    # Step 1: Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_max(arr, n, i)

    # Step 2: Extract elements from the heap
    for i in range(n-1, 0, -1):
        # Move max to the end
        arr[0], arr[i] = arr[i], arr[0]
        # Rebuild heap on the reduced array
        heapify_max(arr, i, 0)

    # Now arr is sorted in ascending order automatically
    return arr


#Example usage
max_heap = [90, 15, 10, 7, 12, 2, 5]
sorted_ascending = heap_sort_ascending(max_heap[:])
print("Sorted ascending:", sorted_ascending)

