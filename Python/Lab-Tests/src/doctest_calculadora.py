import doctest

def soma(x: (int,float), y: int) -> int:
    """
    soma X e Y
    >>> x = 2
    >>> y = 3
    >>> soma(x,y)
    8
    """
    # assert isinstance(x, (int, float)), 'x: int or float'
    # assert isinstance(y, (int, float)), 'y: int or float'
    return x + y

if __name__ == "__main__":
    import doctest

    doctest.testmod()
