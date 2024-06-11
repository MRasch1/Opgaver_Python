def main():    
    for die1 in range(1, 7):  # Outer loop for the first die
        for die2 in range(1, 7):  # Inner loop for the second die
            print(f"({die1}, {die2})")  # Print the combination
if __name__ == "__main__":
    main()
