SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one: list, list_two: list):
    a = str(list_one)[1:-1]
    b = str(list_two)[1:-1]

    if a == b: return EQUAL
    if a in b: return SUBLIST
    if b in a: return SUPERLIST
    return UNEQUAL
