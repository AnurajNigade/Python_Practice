# Write a program to check if a number is a happy number.
def length_of_longest_substring(s):
    char_index = {}  # To store the index of each character in the string
    start = 0  # Start of the current substring
    max_length = 0  # Length of the longest substring without repeating characters

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1

        char_index[s[end]] = end
        current_length = end - start + 1
        max_length = max(max_length, current_length)

    return max_length

# Example usage:
s = "abcdabcdemkbb"
output = length_of_longest_substring(s)
print(output)
