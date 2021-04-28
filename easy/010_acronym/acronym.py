import re

def abbreviate(words):
    '''Make the acronym of a given phrase. Each letter in the acronym represents each word in the phrase. Each word is separated by space and hypen'''
    acronim = ""
    split_words = re.split(r'[ -]', words)
    for word in split_words:
        if word == "":
            continue
        word = word.strip("_")  # Strip only underscore because that's the existing problem at test
        acronim += word[0]
    return acronim.upper()
