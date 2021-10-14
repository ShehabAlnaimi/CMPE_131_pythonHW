import time


def calculate_time(func):
    """
	Take func as parameter
    return func
   """

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        total_time = end_time - start_time
        print(f'Total time {total_time}')

    return wrapper


@calculate_time
def test():
    time.sleep(2)


test()
