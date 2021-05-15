from math import ceil

def cipher_text(plain_text: str):
    plain_text = "".join(i.lower() for i in plain_text if i.isalnum())
    if plain_text:
        column = ceil(len(plain_text) ** 0.5)
        row = ceil(len(plain_text) / column)
        return " ".join(f"{plain_text[i::column]:<{row}}" for i in range(column))

