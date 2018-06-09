def is_leap_year(year):
    """ Checks whether or not a given year[YYYY] is a leap year.
        Returns True or False for provided year.
    """
    return (year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0))

