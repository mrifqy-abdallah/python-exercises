VOWELS = ("a", "i", "u", "e", "o")
SPECIALS = ("xr", "yt")
SUFFIX = "ay"

def translate(text: str):
    text = text.lower().split()
    return " ".join(translate_word(word) for word in text)

def translate_word(word: str):
    return arrange_word(word) + SUFFIX

def arrange_word(word: str):
    if word.startswith(VOWELS) or word.startswith(SPECIALS) or (word.startswith("y") and word[1] not in VOWELS):
        return word
    elif word.startswith("qu"):
        return word[2:] + "qu"
    else:
        return arrange_word(word[1:] + word[0])