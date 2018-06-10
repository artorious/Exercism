""" Test if a year is leap. """


def is_leap_year(year):
    """ (int) -> bool

        Checks whether or not a given year[YYYY] is a leap year.
        Only accepts years represented as integer values
        Returns True or False for provided year.
    """
    try:
        return (year % 4 == 0) and (not(year % 100 == 0) or
                                    (year % 400 == 0))

    except TypeError:
        raise TypeError('Argument should be an integer')
