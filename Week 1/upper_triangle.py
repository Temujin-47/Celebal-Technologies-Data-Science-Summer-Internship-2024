def print_isosceles_upper_triangle(n):
    """
    Function to print an isosceles upper triangle of '*' with n rows.

    Args:
    n: int - number of rows in the triangle
    """
    for i in range(n):
        # Print leading spaces
        for j in range(i):
            print(' ', end=' ')

        # Print stars
        for k in range(n - i):
            print('*', end=' ')

        print()


# Example usage:
n = 5
print_isosceles_upper_triangle(n)
