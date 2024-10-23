# Now prints a rectangle but uses more complicated code

def print_hollow_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            # Print the top and bottom edges of the rectangle
            print('*' * width)
        else:
            # Prints the sides of the rectangle and the space in the middle
            print('*' + ' ' * (width - 2) + '*')

# Call the function with a width of 6 and a height of 4
print_hollow_rectangle(6, 4)

# And let's run to see the results