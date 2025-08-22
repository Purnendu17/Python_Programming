def max_score_split(s):
    max_score = 0

    for i in range(1, len(s)):  # Split points from 1 to len(s)-1
        left = s[:i]  # Left substring
        right = s[i:]  # Right substring

        # Count zeros in the left substring and ones in the right substring
        score = left.count('0') + right.count('1')

        # Update the maximum score
        max_score = max(max_score, score)

    return max_score

# Test the function
test_string = "011101"
result = max_score_split(test_string)
print(f"The maximum score for splitting '{test_string}' is: {result}")
