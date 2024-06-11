def interleave(*lists):
    interleaved_list = []
    for elements in zip(*lists):
        interleaved_list.extend(elements)
    return interleaved_list

# Test cases
def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))  # Expected output: [1, 20, 'a', 2, 30, 'b', 3, 40, 'c']
    print(interleave([1, 2], [3, 4], [5, 6]))                  # Expected output: [1, 3, 5, 2, 4, 6]
    print(interleave([7, 8, 9], [10, 11, 12]))                 # Expected output: [7, 10, 8, 11, 9, 12]
    print(interleave(['x', 'y'], ['a', 'b'], ['1', '2']))      # Expected output: ['x', 'a', '1', 'y', 'b', '2']

if __name__ == "__main__":
    main()
