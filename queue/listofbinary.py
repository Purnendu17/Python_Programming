from collections import deque

def generate_binary_numbers(n):
    queue = deque()
    queue.append("1")
    
    result = []
    
    for _ in range(n):
        front = queue.popleft()  # Get the front element
        result.append(front)  # Store it in result
        
        # Generate next binary numbers
        queue.append(front + "0")
        queue.append(front + "1")
    
    return result

# Example usage
n = int(input("Enter a number: "))
binary_numbers = generate_binary_numbers(n)
print(binary_numbers)
