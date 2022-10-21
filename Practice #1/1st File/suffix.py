# Zahir Choudhry
# Practice Hack-a-thon #3

def common_suffix(word1, word2):
    word = ""

    for i in range(len(word1)):
        for j in range(len(word2)):
            if (word1[i:] == word2[j:]):
                word = word1[i:]
                return word


    """Find the common suffix of two words.

    Arguments:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        str: The common characters at the end of the two words, or the empty
            string if the words do not share a common suffix.

    Examples:

        >>> print(common_suffix("argument", "endorsement"))
        ment

        >>> print(common_suffix("identical", "identical"))
        identical

        In the following example, the two words have no letters in common, so
        the function returns the empty string. I print it between arrows to show
        that a result is returned, but is empty.

        >>> result = common_suffix("distinguished", "distinguishable")
        >>> print("-->" + result + "<--")
        --><--

        More examples.

        >>> result = common_suffix("", "")
        >>> print("-->" + result + "<--")
        --><--

        >>> result = common_suffix("", "irrelevant")
        >>> print("-->" + result + "<--")
        --><--

        >>> result = common_suffix("irrelevant", "")
        >>> print("-->" + result + "<--")
        --><--

    """
    pass # FIXME

print(common_suffix("argument", "endorsement"))