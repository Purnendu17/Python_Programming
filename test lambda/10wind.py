from collections import defaultdict

def find_sub_string(s):
    str_len = len(s)
    dist_count_char = len(set(s))

    ctr, start_pos, start_pos_index, min_len = 0, 0, -1, float('inf')
    curr_count = defaultdict(int)

    for i in range(str_len):
        curr_count[s[i]] += 1
        if curr_count[s[i]] == 1:
            ctr += 1
        if ctr == dist_count_char:
            while curr_count[s[start_pos]] > 1:
                curr_count[s[start_pos]] -= 1
                start_pos += 1
            current_window_len = i - start_pos + 1
            if current_window_len < min_len:
                min_len = current_window_len
                start_pos_index = start_pos

    if start_pos_index != -1:
        return f"Smallest window is from index {start_pos_index} to {start_pos_index + min_len - 1}, length {min_len}"
    else:
        return "No valid window found"

input_string = "abcdgabcdkjhfddfbac"
result = find_sub_string(input_string)
print(result)
