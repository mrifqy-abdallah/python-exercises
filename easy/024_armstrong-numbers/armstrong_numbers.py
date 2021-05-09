def is_armstrong_number(number:int):
    number = str(number)
    armstrong = 0
    length = len(number)
    for i in number:
        armstrong += int(i) ** length
    return int(number) == armstrong
