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
    ic_list = []
    if keyword == "even":  # четные
        ic_list = list(filter(lambda v: v % 2 == 0, list_int))
    elif keyword == "odd":  # нечетные
        ic_list = list(filter(lambda v: v % 2 != 0, list_int))
    elif keyword == "prime":  # простые
        for i in list_int:
            count = 0
            for j in range(2, 10):
                if i % j == 0:
                    count += 1
            if i < 10 and count < 2:
                ic_list.append(i)
            elif i > 10 and count == 0:
                ic_list.append(i)
    return ic_list

print("Test int_conversion:", int_conversion([1, 4, 5, 6, 7, 100, 10, 11, 13, 17], "prime"))

# TODO change def int_conversion
