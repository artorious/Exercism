""" Function to test for pangrams. """
import string


def is_pangram(sentence):
    """ Test if a <sentence> is a pangram.

        Returns True or False
    """
    if isinstance(sentence, str):
        return set(string.ascii_lowercase).issubset(set(sentence.lower()))
    else:
        raise TypeError('Expected  a string.')
