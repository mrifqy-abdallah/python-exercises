def rebase(input_base: int, digits: 'list[int]', output_base: int) -> 'list[int]':
    if input_base < 2 or output_base < 2:
        raise ValueError("Value of input base and output base must be 2 or greater.")

    if not all(map(lambda x: x >= 0 and x < input_base, digits)):
        raise ValueError("Digits has invalid value (must be positive number and less than input base).")

    # Quick return
    if not digits or digits.count(0) == len(digits):
        return [0]

    return convert_int_to_digits_base(convert_digits_base_to_int(input_base, digits), output_base)


def convert_digits_base_to_int(base: int, digits: 'list[int]') -> int:
    result = 0
    seq = len(digits) - 1
    for i in digits:
        result += i * base**seq
        seq -= 1
    return result


def convert_int_to_digits_base(number: int, base: int) -> 'list[int]':
    result = []
    while number >= 1:
        number, remainder = divmod(number, base)
        result.append(remainder)
    
    return result[::-1]

