import operator
from string import ascii_lowercase
from secrets import SystemRandom

CHARACTERS = ascii_lowercase
s = SystemRandom().choices

class Cipher:
    def __init__(self, key:str = None):
        if key:
            self.key = key.lower()
        else:
            self.key = "".join(s(CHARACTERS, k=100))

    def encode(self, text:str):
        self.text = text.lower()
        return self.substitute(operator.add)

    def decode(self, text:str):
        self.text = text.lower()
        return self.substitute(operator.sub)

    def substitute(self, operation:operator):
        result = ""
        for i, char in enumerate(self.text):
            distance = CHARACTERS.index(self.key[i % len(self.key)])
            result += CHARACTERS[operation(CHARACTERS.index(char), distance) % 26]
        return result
