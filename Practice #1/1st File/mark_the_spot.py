# Zahir Choudhry
# Practice Hack-a-thon #2

def mark_the_spot(grid):
    # print("LOL")
    for i in range(len(grid)):
            # print("Cherry")
            grid[i][i] = "X"
    for j in range(len(grid)):
            # print("Banana Bread")
            grid[(len(grid)-1)-j][j] = "X"
    
    return grid
    
    
    """Draw an X in a 2D grid.

    Given a 2D grid (ie. a nested list of strings), replace specific squares
    with "X" (the capital X) to draw a larger X from corner to corner.

    Arguments:
        grid (list): A nested list of size N by N, filled with spaces (" ").
            Assume N is positive and odd.

    Returns:
        list: The modified nested list with an X that goes from corner to corner.

    Examples:

        Note that although I print out each row by itself for clarity, the
        return value should be a nested list.

        >>> grid = [ \
                [" ", " ", " "], \
                [" ", " ", " "], \
                [" ", " ", " "], \
            ]
        >>> result = mark_the_spot(grid)
        >>> for row in result:
        ...     print(row)
        ...
        ['X', ' ', 'X']
        [' ', 'X', ' ']
        ['X', ' ', 'X']

        >>> grid = [ \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
            ]
        >>> result = mark_the_spot(grid)
        >>> for row in result:
        ...     print(row)
        ...
        ['X', ' ', ' ', ' ', ' ', ' ', 'X']
        [' ', 'X', ' ', ' ', ' ', 'X', ' ']
        [' ', ' ', 'X', ' ', 'X', ' ', ' ']
        [' ', ' ', ' ', 'X', ' ', ' ', ' ']
        [' ', ' ', 'X', ' ', 'X', ' ', ' ']
        [' ', 'X', ' ', ' ', ' ', 'X', ' ']
        ['X', ' ', ' ', ' ', ' ', ' ', 'X']

    """
    pass # FIXME

grid = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        ]

result = mark_the_spot(grid)
for row in result:
    # print("APPLES")
    print(row)