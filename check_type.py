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
        def type_check(object_to_check_type: object):
            """
            Checks whether the function receives the correct type object according to the decorator if no error is sent.
            :param object_to_check_type: Object to check type.
            :return:None
            """
            if type(object_to_check_type) != correct_type:
                raise Exception("Wrong object type")
            return func(object_to_check_type)
        return type_check
    return decorator


@decorator_factory(list)
def average_calculation(list_of_numbers: list) -> float:
    """
    A function that gets a list of numbers and returns their average.
    :param list_of_numbers:List of numbers to calculate average.
    :return:Average of the list numbers.
    """
    return sum(list_of_numbers)/len(list_of_numbers)


if __name__ == '__main__':
    list_of_numbers_to_average = [1, 2, 3, 4]
    name = "ortal"
    print(average_calculation(list_of_numbers_to_average))
    print(average_calculation(name))
