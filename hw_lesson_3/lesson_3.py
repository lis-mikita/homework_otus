# Homework of lesson 3

def square_of_numbers(keyword, *args):
    """
    :param args: N integer
    :param keyword: Choice of degree of N integer
    :return: list of square N integer
    """
    son_list = []
    return [v ** keyword for v in args]

def int_conversion(list_int, keyword):
    """
    :param list_int:
    :param keyword:
    :return:
    """
    ic_list = list_int
    if keyword == "even":
        pass
    elif keyword == "odd":
        pass
    elif keyword == "prime":
        pass
    else:
        pass
    return ic_list
# TODO add feature for def int_conversion