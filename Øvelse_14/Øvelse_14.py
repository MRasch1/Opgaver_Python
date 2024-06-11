def find_matching(strings, search_string):
    matching_indices = []
    for index, string in enumerate(strings):
        if search_string in string:
            matching_indices.append(index)
    return matching_indices

# Example usage
print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))  # Output: [0, 1, 3]
