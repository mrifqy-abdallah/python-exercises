import string

def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    # Extract alphabets from the sentence
    clean_sentence = [i.lower() for i in sentence if i.isalpha()]

    return set(alphabet) == set(clean_sentence)
