'''
Actually there's a module for this, called python-rle.
But the module require input in a different format than given here.
So we're not going to use that..
'''

def encode(string: str):
    encoded_string = ""
    if string != "":
        char = string[0]
        count = 1
        for i in string[1:]:
            if i == char:
                count += 1
            else:
                # In case if a character only shown once like 'XYYY', 
                # so the encoded will be 'X3Y' and not '1X3Y'
                encoded_string += str(count) if count > 1 else ""
                encoded_string += char
                # Reset variable's value
                char = i
                count = 1
        # Add the last detected character to encoded_string
        else:
            encoded_string += str(count) if count > 1 else ""
            encoded_string += char
    return encoded_string


def decode(string):
    decoded_string = ""
    if string != "":
        # In case of double-digit value like '12W', therefore count needs to become a string and not int
        count = ""
        for i in string:
            if i.isdigit():
                count += i
            elif i.isalpha() or i.isspace():
                # In case of implicit digit value like 'XYZ' (actually is '1X1Y1Z')
                count = "1" if count == "" else count
                decoded_string += i * int(count)
                # Reset count
                count = ""
    return decoded_string
    