from functools import wraps


def decorator_factory(correct_type: type):
    """
    A decorator that gets an object type
    and returns a decorator that checks if the variable type is the type of object that the function gets.
    :param correct_type: The correct object type.
    :return: decorator function
    """
    def decorator(func: callable):
        """
        A decorator that checks whether the function gets the variable of the correct type.
        If it is incorrect, an error message is sent.
        :param func:The function that receives an object.
        :return:The function it gets.
        """
        @wraps(func)
        def type_check(obj: object):
            """
        Checks whether the function receives the correct type object  according to the decorator if no error is sent.
            :param obj: Object to test
            :return:None
            """
            if type(obj) != correct_type:
                raise Exception('Wrong object type')
            return func(obj)
        return type_check
    return decorator


@decorator_factory(int)
def times2(num):
    return num*2


if __name__ == '__main__':
    print(times2(2))
    save_num = times2("ortal")
    print(save_num)
