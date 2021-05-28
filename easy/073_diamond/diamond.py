from string import ascii_uppercase


def rows(letter: str) -> 'list[str]':
    letter = letter.upper()
    if letter not in ascii_uppercase:
        raise ValueError("Input must be alphabet.")
    if len(letter) != 1:
        raise ValueError("You must insert exactly one alphabet.")

    # Quick return
    if letter == "A":
        return ["A"]

    index_of_letter = ascii_uppercase.index(letter)
    total_spaces = index_of_letter * 2 + 1
    result = []
    half_below = []

    # Initiate adding the opening 'A'
    result.append(f"{'A':^{total_spaces}}")
    # Initiate adding the closing 'A'
    half_below.append(f"{'A':^{total_spaces}}")

    for i in range(1, index_of_letter + 1):
        char = ascii_uppercase[i]
        center_spaces = i * 2 - 1
        shape = f"{char}{' ' * center_spaces}{char}"

        # This condition gets executed at the last `i`
        if i == index_of_letter:
            result.append(shape)
            result.extend(half_below)
        else:
            shape = f"{shape:^{total_spaces}}"
            half_below.insert(0, shape)
            result.append(shape)    

    return result
