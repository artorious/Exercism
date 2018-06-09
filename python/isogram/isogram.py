""" Tests if a word or phrase is an isogram """


def is_isogram(string):
    """ (str) -> bool

        Checks if a string is an isogram.
        Returns True if it is, else, returns False
        NOTE: An isogram is a word or phrase without a repeating letter
    """
    if isinstance(string, str):
        string = string.strip().lower()
        accepted_chars = (' ', '  ', '-')
        isogram = True

        for letter in string:
            if letter not in accepted_chars:
                letter_count = string.count(letter)
                if letter_count > 1:
                    isogram = False
        return isogram
    else:
        return 'Expected a string'
