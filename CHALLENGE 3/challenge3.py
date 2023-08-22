def solve(s):
    def get_consonant_value(substr):
        consonant_value = 0
        for char in substr:
            consonant_value += ord(char) - ord('a') + 1
        return consonant_value

    consonant_substrings = []
    current_substring = "" 

    for char in s:
        if char not in "aeiou":
            current_substring += char
        else:
            if current_substring:
                consonant_substrings.append(current_substring)
            current_substring = ""

    if current_substring:
        consonant_substrings.append(current_substring)

    max_value = 0
    for substr in consonant_substrings:
        value = get_consonant_value(substr)
        if value > max_value:
            max_value = value

    return max_value


# Test cases
print(solve("shercie"))  # Output: 27
print(solve("memer"))  # Output: 18
