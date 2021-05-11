def encode(plain_text: str):
    plain_text = plain_text.lower()
    encoded = []
    encoded_partial = ""

    for char in plain_text:
        if char.isalpha():
            encoded_partial += chr(abs(ord(char) % 97 - 122))  
            # Because a-z is 97-122 in unicode,
            # And we use abs because the equation's result will be negative
        elif char.isdigit():
            encoded_partial += char
        
        if len(encoded_partial) == 5:
            encoded.append(encoded_partial)
            encoded_partial = ""

    # In case the iteration above has finished and encoded_partial still has a value
    if encoded_partial:
        encoded.append(encoded_partial)
    
    return " ".join(encoded)


def decode(ciphered_text: str):
    ciphered_text = ciphered_text.lower()
    decoded = ""
    
    for char in ciphered_text:
        if char.isalpha():
            decoded += chr(abs(ord(char) % 97 - 122))
        elif char.isdigit():
            decoded += char
    
    return decoded
