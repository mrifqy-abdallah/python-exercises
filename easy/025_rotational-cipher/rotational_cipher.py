def rotate(text:str, key:int):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + key-65) % 26 + 65)  # Because A-Z is 65-90 (26 in total) in unicode
        elif char.islower():
            result += chr((ord(char) + key-97) % 26 + 97)  # Because a-z is 97-122 in unicode
        else:
            result += char
    
    return result
