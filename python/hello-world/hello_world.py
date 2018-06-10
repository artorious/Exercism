""" Hello World """


def hello(name=''):
    """ (str) -> str

        Returns "Hello <name>!" when param is provided.
        Else, "Hello World!"
    """
    if isinstance(name, str):
        if name.strip() == '':
            return 'Hello, World!'
        else:
            return 'Hello, {}!'.format(name)
    else:
        raise TypeError('Argument should be a string')
