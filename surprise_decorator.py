def change_original_functionality_decorator(func: callable):
    """
    A decorator that will make the function print “surprise!” instead of its original functionality.
    :param func:The original function.
    :return:The function print_surprise.
    """
    def print_surprise():
        print("surprise!")
    return print_surprise


@change_original_functionality_decorator
def print_name():
    print("print name")


if __name__ == '__main__':
    print_name()
