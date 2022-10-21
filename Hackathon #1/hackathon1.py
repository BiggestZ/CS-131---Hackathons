# Zahir Choudhry
# 10 / 7 / 2021
# Hack a thon #1

# Question 1
def can_order(num_instock, num_inprocess, num_ordered):
    
    if (num_instock < 0 or num_ordered < 0): #Keepts them non negative numbers
        return False
    
    if (num_inprocess + num_ordered <= num_instock):
        return True
    else:
        return False

    # num_instock is non negative
    # num_inprocess can be +-
    # num_ordered is non negative    
    """Determine if an online Oxy T-shirt order can be fulfilled.

    Arguments:
        num_instock (int): The number of t-shirts currently in stock. This number is non-negative.
        num_inprocess (int): The number of t-shirts ordered but not yet processed.
            This argument can be positive or negative, as t-shirts may be returned.
            num_ordered (int): This is the number of t-shirts requested in the current order.

    Returns:
        bool: True if the order can be successfully processed, False if there aren't enough t-shirts in stock.

    Examples:

        An order can be processed when the number of t-shirts ordered and in process does not exceed the number of t-shirts in stock

        >>> print(can_order(12, 10, 1))
        True

        >>> print(can_order(10, 10, 1))
        False

        >>> print(can_order(7, 10, 2))
        False
        
        >>> print(can_order(12, -10, 10))
        True

         >>> print(can_order(12, 10, -5)) #can't fulfill a negative order
        False 

    """
    pass #FIXME


# Question 2
def mark_the_spot(grid, sign):
    for i in range(len(grid)):
            # print("Cherry")
            grid[i][i] = sign
    for j in range(len(grid)):
            # print("Banana Bread")
            grid[(len(grid)-1)-j][j] = sign
    
    return grid
    """Draw an X in a 2D grid.

   Given a 2D grid (ie. a nested list of strings), replace specific squares
    to form an "X" (the capital X) from corner to corner, using character in sign.

    Arguments:
        grid (list): A nested list of size N by N, filled with spaces (" ").
            Assume N is positive and odd.
        sign (char): A typographic character with which to fill the X

    Returns:
        list: The modified nested list with a large X that goes from corner to corner.

    Examples:

        Note that although I print out each row by itself for clarity, the
        return value should be a nested list.

        >>> grid = [ \
                [" ", " ", " "], \
                [" ", " ", " "], \
                [" ", " ", " "], \
            ]
        >>> result = mark_the_spot(grid, 'X')
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
        >>> result = mark_the_spot(grid, '#')
        >>> for row in result:
        ...     print(row)
        ...
        ['#', ' ', ' ', ' ', ' ', ' ', '#']
        [' ', '#', ' ', ' ', ' ', '#', ' ']
        [' ', ' ', '#', ' ', '#', ' ', ' ']
        [' ', ' ', ' ', '#', ' ', ' ', ' ']
        [' ', ' ', '#', ' ', '#', ' ', ' ']
        [' ', '#', ' ', ' ', ' ', '#', ' ']
        ['#', ' ', ' ', ' ', ' ', ' ', '#']

    """
    pass # FIXME


# Question 3
def common_word(string1, string2):
    list = []
    u_list = []

    str_1 =string1.lower()
    str_2 = string2.lower()

    s_1 = str_1.split(" ")
    s_2 = str_2.split(" ")

    # print (s_1)
    # print (s_2)

    if (str_1 == "" or str_2 == ""):
        return list

    for i in range(len(s_1)):
        for j in range(len(s_2)):
            if( s_1[i] == s_2[j] ):
                if (s_1[i] not in list):
                    list.append(s_1[i])
    return list

    """for k in range(len(list)):
        if (list[k] not in u_list):
            u_list.append(list[k])
        return u_list"""
    """for b in range(len(u_list)):
            print(u_list[b] + "1")
            if (u_list[b] != list[k]):
                #print(u_list[b])
                #print(list[k])
                u_list.append(list[k])
                print(u_list[b])
                # print(list[k])
                break"""


    """Find the list of unique common words in two strings.

    Arguments:
        string1 (str): The first string, no punctuation.
        string2 (str): The second string, no punctuation.

    Returns:
        str: The list contains common words of the two strings, or the empty
             list if the words do not share a common word. Words returned should be 
             lowercase and should not contain punctuation.

    Examples:

        >>> print(common_word("hello world", "peace in the world"))
        ['world']

        >>> print(common_word("identical", "identical"))
        ['identical']

        In the following example, the two words have no letters in common, so
        the function returns empty list. 

        >>> result = common_word("CS131 is my favorite class", "Computer science majors are super fun")
        >>> print(result)
            []

        >>> result = common_word("", "")
        >>> print(result)
            []


    """
    pass #FIXME

""" TEST CASES FOR T SHIRT : COMPLETE
print(can_order(12, 10, 1))
print(can_order(10, 10, 1))
print(can_order(7, 10, 2))
print(can_order(12, -10, 10))
print(can_order(12, 10, -5))  # can't fulfill a negative order
"""

""" TEST CASES FOR GRID: COMPLETE
grid = [
       [" ", " ", " "], \
       [" ", " ", " "], \
       [" ", " ", " "], \
       ]
result = mark_the_spot(grid, 'X')
for row in result:
    print(row)

grid = [ \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
                [" ", " ", " ", " ", " ", " ", " "], \
            ]
result = mark_the_spot(grid, '#')
for row in result:
    print(row)
"""

# TEST OF COMMON WORD: COMPLETE
"""
print(common_word("identical", "identical"))

print(common_word("hello world", "hello in the world"))

result = common_word("CS131 is my favorite class", "Computer science majors are super fun")
print(result)

result = common_word("", "")

print(result) 
"""
# print(common_word('Happy birthday to all the October peeps', 'This hackathon is making me really happy'))

print(common_word('This is the LAST TEST for the hackathon', "The moment happened where I didn't think I could last this long in the hackathon"))