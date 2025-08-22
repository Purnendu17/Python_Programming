def find_celebrity(adj_list, n):
    # Step 1: Candidate Selection
    celeb = 0  # Assume 0 is the celebrity

    for i in range(1, n):
        if i in adj_list.get(celeb, []):  # If celeb knows i, they can't be a celeb
            celeb = i  # Update potential celebrity

    # Step 2: Verify the candidate
    for i in range(n):
        if i != celeb:
            # The celebrity should not know 'i', but 'i' should know the celebrity
            if celeb in adj_list.get(i, []) and celeb not in adj_list.get(celeb, []):
                continue
            else:
                return -1  # Not a valid celebrity

    return celeb  # Return the index of the celebrity

# Example Input: Adjacency List Representation
adj_list = {
    0: [1],  # Person 0 knows 1
    1: [],   # Person 1 knows no one (Potential celebrity)
    2: [1]   # Person 2 knows 1
}

n = 3  # Number of people
print("Celebrity is:", find_celebrity(adj_list, n))  
