def distinct_characters(strings):
    result = {}
    for s in strings:
        distinct_char_count = len(set(s))
        result[s] = distinct_char_count
    return result

# Example usage
print(distinct_characters(["check", "look", "try", "pop"]))  # Output: {'check': 4, 'look': 3, 'try': 3, 'pop': 2}
