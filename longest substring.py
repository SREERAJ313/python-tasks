def longest_unique_substring(s):
    start = 0
    max_length = 0
    max_substring = ""
    char_index_map = {}
    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        if end - start + 1 > max_length:
            max_length = end - start + 1 
            max_substring = s[start:end + 1]
    return max_substring
input_string = "abcabcbb"
result = longest_unique_substring(input_string)
print("Input String:", input_string)
print("Longest Substring with Unique Characters:", result)