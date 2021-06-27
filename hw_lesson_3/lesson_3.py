# Homework of lesson 3

from functools import wraps
from time import time
from pprint import pprint

def timing_dec(func, *args):
    @wraps(func)
    def wrapper(*args):
        start_time = time()
        func(*args)
        return time() - start_time
    return wrapper

@timing_dec
def square_of_numbers_dec(keyword, *args):
    """
    :param args: N integer
    :param keyword: Choice of degree of N integer
    :return: list of square N integer
    """
    son_list = []
    return [v ** keyword for v in args]

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
    :param list_int: input list of numbers
    :param keyword: "even" or "odd" or "prime"
    :return: sorter list
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

def count_input_dec(func, *args):
    @wraps(func)
    def wrapper(*args):
        res = func(*args)
        count_input_dec.cif += 1
        print("The number of entries into the function:", count_input_dec.cif)
        return res
    return wrapper

count_input_dec.cif = 0

@count_input_dec
def fib(n=2):
    f0, f1, step = 0, 1, "____"
    if n >= 0:
        if n == 0:
            print(f"fib({f0}):", f0)
            return {f0: f0}
        elif n == 1:
            print(f"fib({f0}):", f0)
            print(step + ' ' + f"fib({f1}):", f1)
            return {f0: f0, f1: f1}
        else:
            print(f"fib({f0}):", f0)
            print(step + ' ' + f"fib({f1}):", f1)
            res = {f0: f0, f1: f1}
            for i in range(2, n+1):
                res[i] = res[i-1] + res[i-2]
                print(step*i + ' ' + f"fib({i}):", res[i])
            return res
    else:
        print(f"fib({f1}):", f1)
        print(f"fib({f0}):", f0)
        res = {f1: f1, f0: f0}
        for i in range(-1, n-1, -1):
            res[i] = res[i + 2] - res[i + 1]
            print(f"fib({i}):", res[i], step * abs(i))
        return res


print("Show work function square_of_numbers:")
print("Square of 1, 3, 4, 120, 1000 of degree 1:", square_of_numbers(1, 1, 3, 4, 120))
print("Square of 1, 3, 4, 120, 1000 of degree 2:", square_of_numbers(2, 1, 3, 4, 120))
print("Square of 1, 3, 4, 120, 1000 of degree 10:", square_of_numbers(10, 1, 3, 4, 120))

print("Show work timing_dec for function square_of_numbers:")
print("Time build square of 1, 3, 4, 120, 1000 of degree 1:", square_of_numbers_dec(1, 1, 3, 4, 120))
print("Time build square of 1, 3, 4, 120, 1000 of degree 2:", square_of_numbers_dec(2, 1, 3, 4, 120))
print("Time build square of 1, 3, 4, 120, 1000 of degree 10:", square_of_numbers_dec(10, 1, 3, 4, 120))

print("Show work function int_conversion:")
my_list = [1, 3, 4, 9, 13, 120, 1000]
print("List =", my_list)
print("Filter 'even' in my_list:", int_conversion(my_list, "even"))
print("Filter 'odd' in my_list:", int_conversion(my_list, "odd"))
print("Filter 'prime' in my_list:", int_conversion(my_list, "prime"))

print("Calculation fib 10:", fib(10))
print("Calculation fib -10:", fib(-10))
pprint(fib(4))
