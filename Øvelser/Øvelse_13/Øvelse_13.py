def reverse_dictionary(d):
    reversed_dict = {}
    for english_word, finnish_words in d.items():
        for finnish_word in finnish_words:
            if finnish_word not in reversed_dict:
                reversed_dict[finnish_word] = []
            reversed_dict[finnish_word].append(english_word)
    return reversed_dict

# Example usage
d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
print(reverse_dictionary(d))  # Output: {'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}
