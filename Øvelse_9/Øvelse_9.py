def merge(L1, L2):
    i, j = 0, 0
    merged_list = []
    
    # Iterate through both lists and merge them in sorted order
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged_list.append(L1[i])
            i += 1
        else:
            merged_list.append(L2[j])
            j += 1
            
    # If there are remaining elements in L1, add them to merged_list
    while i < len(L1):
        merged_list.append(L1[i])
        i += 1
        
    # If there are remaining elements in L2, add them to merged_list
    while j < len(L2):
        merged_list.append(L2[j])
        j += 1
    
    return merged_list

# Test cases
L1 = [1, 3, 5, 7]
L2 = [2, 4, 6, 8]
print(merge(L1, L2))  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8]

L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(merge(L1, L2))  # Expected output: [1, 2, 3, 4, 5, 6]

L1 = [1, 1, 1, 1]
L2 = [1, 1, 1, 1]
print(merge(L1, L2))  # Expected output: [1, 1, 1, 1, 1, 1, 1, 1]

L1 = []
L2 = [1, 2, 3]
print(merge(L1, L2))  # Expected output: [1, 2, 3]

L1 = [4, 5, 6]
L2 = []
print(merge(L1, L2))  # Expected output: [4, 5, 6]
