def minmax(*args):
    """
    Find minimum and maximum values simultaneously.

    Example
    -------
    >>> minmax(2, 1, 4, 3)
    (1, 4)
    >>> minmax([2, 1, 4, 3])
    (1, 4)

    """
    if len(args) > 1:
        return minmax(args)
    iterable = iter(args[0])
    min = max = iterable.next()
    for item in iterable:
        if item < min:
            min = item
        elif item > max:
            max = item
    return min, max

def test_minmax():
    assert minmax(2, 1, 4, 3) == (1, 4)
    assert minmax([2, 1, 4, 3]) == (1, 4)
