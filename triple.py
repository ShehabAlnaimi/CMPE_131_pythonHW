def tripler(func):
    """
    take func as parameter and return wrapper
    """
    def wrapper():
        for call in range(0, 3):
            func()

    return wrapper


@tripler
def test():
    print('call')


test()
