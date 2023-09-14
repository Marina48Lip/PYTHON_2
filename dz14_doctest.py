def Triangle(a, b, c):

    """
    >>> Triangle(2, 3, 4)
    'Треугольник разносторонний'

    >>> Triangle(3, 3, 4)
    'Треугольник разносторонний'

    """


    if a + b < c or a + c < b or c + b < a:
        return "Такого треугольника не существует"
    elif a == b == c:
        return 'Треугольник равносторонний'
    elif a != b != c:
        return 'Треугольник разносторонний'
    else:
        return 'Треугольник равнобедренный'


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)