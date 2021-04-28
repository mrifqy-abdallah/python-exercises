import re

def count_words(sentence):
    '''Count the occurrences of each word in the given phrase. Each word are separated with spaces, commas, underscores, new lines, and tabs.'''
    punc = '''!()-[]{};:"\\, <>./?@#$%^&*_~'''  # single-quote are excluded from here
    sentence = re.split(r'[ _,\r\n\r\t]', sentence.lower())
    count_each_words = {}
    for word in sentence:
        clean_word = word.strip("'")  # single-quote gets removed only if it's at the edge 
        for i in word:
            if i in punc:
                clean_word = clean_word.replace(i, "")
        if clean_word == '':
            continue
        if clean_word not in count_each_words:
            count_each_words[clean_word] = 0
        count_each_words[clean_word] += 1
    return count_each_words

