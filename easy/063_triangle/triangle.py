def equilateral(sides: 'list[int, int, int]') -> bool:
    return is_valid_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: 'list[int, int, int]') -> bool:
    return is_valid_triangle(sides) and len(set(sides)) <= 2


def scalene(sides: 'list[int, int, int]') -> bool:
    return is_valid_triangle(sides) and len(set(sides)) == 3


def is_valid_triangle(sides: 'list') -> bool:
    # Return True if the triangle is valid, False otherwise
    sides_is_more_than_zero = all(map(lambda x: x > 0, sides))
    smallest, medium, biggest = sorted(sides)

    return len(sides) == 3 and smallest + medium >= biggest and sides_is_more_than_zero
