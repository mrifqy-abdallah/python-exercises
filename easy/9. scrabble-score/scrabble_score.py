def score(word):
    value_of_letters = {
        "A": 1, "B": 3, "C": 3, "D": 2, "E": 1,
        "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
        "K": 5, "L": 1, "M": 3, "N": 1, "O": 1,
        "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1,
        "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
    }
    total_value = 0
    word = word.upper()
    for i in word:
        if i in value_of_letters.keys():
            total_value += value_of_letters.get(i)
    return total_value
