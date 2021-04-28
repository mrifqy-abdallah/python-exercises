def is_isogram(string):
    # replace hyphens and spaces from string, then make it lowercase
    string = string.replace("-", "").replace(" ", "").lower()

    if len(string) != len(set(string)):
        return False
    return True
