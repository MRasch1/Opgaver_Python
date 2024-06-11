def transform(str1, str2):
    # Split the strings into words and convert them to integers
    list1 = list(map(int, str1.split()))
    list2 = list(map(int, str2.split()))
    
    # Use zip to pair the integers and multiply them
    result = [a * b for a, b in zip(list1, list2)]
    
    return result

# Example usage
print(transform("1 5 3", "2 6 -1"))  # Output: [2, 30, -3]
