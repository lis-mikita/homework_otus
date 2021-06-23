# Homework of lesson 3

def square_of_numbers(keyword, *args):
    """
    :param args: N integer
    :param keyword: Choice of degree of N integer
    :return: list of square N integer
    """
    son_list = []
    return [v ** keyword for v in args]
