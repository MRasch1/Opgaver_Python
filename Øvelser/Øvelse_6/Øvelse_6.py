def triple(n):
    return n * 3

def square(n):
    return n ** 2

def main():
    # Part 1: Loop through values 1 to 10
    print("Part 1 Output:")
    for i in range(1, 11):
        t = triple(i)
        s = square(i)
        print(f"triple({i})=={t} square({i})=={s}")
    
    # Adding a separator between part 1 and part 2 outputs
    print("\nPart 2 Output:")
    
    # Part 2: Stop when square is larger than triple
    for i in range(1, 11):
        t = triple(i)
        s = square(i)
        if s > t:
            break
        print(f"triple({i})=={t} square({i})=={s}")

# Run the main function
main()
