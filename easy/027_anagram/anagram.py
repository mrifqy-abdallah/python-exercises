from collections import Counter


def find_anagrams(word: str, candidates: list):
    # Lower the word, split it to list of characters, then map it to a dictionary
    map_word = Counter(list(word.lower()))
    anagrams = []

    for candidate in candidates:
        # Exclude the candidate if it has the exact same word as `word` input
        if candidate.lower() == word.lower():
            continue
        map_candidate = Counter(list(candidate.lower()))
        if map_candidate == map_word:
            anagrams.append(candidate)

    return anagrams
