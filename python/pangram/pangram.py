""" Function to test for pangrams. """


def is_pangram(sentence):
    """ Test if a <sentence> is a pangram.

        Returns True or False
    """
    sentence_lower_set = set(sentence.lower())
    perfect_lower_case_pangram_set = set('abcdefghijklmnopqrstuvwxyz')
    return perfect_lower_case_pangram_set.issubset(sentence_lower_set)
