def detect_ranges(nums):
    if not nums:
        return []
    
    nums.sort()
    result = []
    start = nums[0]
    end = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == end + 1:
            end = nums[i]
        else:
            if start == end:
                result.append(start)
            else:
                result.append((start, end + 1))
            start = nums[i]
            end = nums[i]
    
    if start == end:
        result.append(start)
    else:
        result.append((start, end + 1))
    
    return result

# Test cases
print(detect_ranges([2, 5, 4, 8, 12, 6, 7, 10, 13]))  # Expected output: [2, (4, 9), 10, (12, 14)]
print(detect_ranges([1, 2, 3, 4, 5]))                # Expected output: [(1, 6)]
print(detect_ranges([1, 3, 4, 5, 7, 8, 9]))          # Expected output: [1, (3, 6), (7, 10)]
print(detect_ranges([1, 2, 4, 5, 7, 9]))             # Expected output: [(1, 3), (4, 6), 7, 9]
print(detect_ranges([]))                             # Expected output: []

