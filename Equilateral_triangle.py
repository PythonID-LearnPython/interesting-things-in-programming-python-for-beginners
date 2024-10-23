# Change the code a bit to see the difference

def print_equilateral_triangle(n):
    for i in range(1, n + 1):
        # Print a space at the beginning of the line to center it
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Call the function with row number 5
print_equilateral_triangle(5)

# And let's run to see the results