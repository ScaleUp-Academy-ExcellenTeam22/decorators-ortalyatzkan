import decorator


@decorator.decorator
def do_twice_decorator(func: callable):
    """
    A decorator that a decorator that executes the function it wraps twice.
    :param func:The function that the decorator wraps.
    :return:TA function that calls a function that the decorator wraps twice.
    """
    func()
    func()
    return func


@do_twice_decorator
def print_name():
    """
    A print function.
    :return: None.
    """
    print("hello")


if __name__ == '__main__':
    print_name()
