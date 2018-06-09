""" Hello World """


def hello(name=''):
    """ (str) -> str

        Returns "Hello <name>!" when param is provided.
        Else, "Hello World!"
    """
    if name.strip() == '':
        return 'Hello, World!'
    else:
        return 'Hello, {}!'.format(name)

