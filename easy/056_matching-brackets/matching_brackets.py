from re import sub

BRACKETS = {"(": ")", "[": "]", "{": "}"}

def is_paired(input_string: str):
    input_string = sub(r'[^(){}[\]]', '', input_string)
    match = []

    for i in input_string:
        if i in BRACKETS.keys():
            match.append(i)
        # In case `match` is empty but then there's a closing bracket,
        # OR the closing bracket doesnt match with the last opening bracket
        elif not match or i != BRACKETS[match.pop()]:
            return False

    # Return True if `match` is empty (which means all the brackets is all paired), and False otherwise
    return not match
