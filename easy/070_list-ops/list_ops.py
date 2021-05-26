from functools import reduce

def append(list1: list, list2: list) -> list:
    return list1 + list2


def concat(lists: list) -> list:
    result = []
    for i in lists:
        if i:
            if type(i) is list:
                result.extend(i)
            else:
                result.append(i)
    return result


def filter(function, list: list) -> list:
    return [i for i in list if function(i)]


def length(list: list) -> int:
    if not list:
        return 0
    return reduce(lambda x,_: x+1, list)


def map(function, list: list) -> list:
    return [function(i) for i in list]


def foldl(function, list: list, initial: int) -> int:
    for i in list:
        initial = function(initial, i)
    return initial


def foldr(function, list: list, initial: int) -> int:
    for i in reverse(list):
        initial = function(i, initial)
    return initial


def reverse(list: list) -> list:
    return list[::-1]
