VOWEL_SOUND = ("a", "i", "u", "e", "o", "xr", "yt")

def translate(text: str):
    text = text.lower().split()
    suffix = "ay"
    result = []
    for word in text:
        # In case of Rule 1, where the word starts with a vowel sound
        if word.startswith(VOWEL_SOUND):
            result.append(word + suffix)

        # In case of Rule 3, where there's 'qu' in the word
        elif "qu" in word:
            qu_index = word.index("qu")
            # In case 'qu' is the beginning of the word
            if qu_index == 0:  
                result.append(word[2:] + "qu" + suffix)
                continue
            # In case 'qu' is not the beginning, check if its prior letter is a vowel
            if word[qu_index-1] not in VOWEL_SOUND:
                result.append(word[qu_index+2:] + word[qu_index-1:qu_index+2] + suffix)
            else:
                result.append(word[qu_index+2:] + word[:qu_index+2] + suffix)

        else:
            vowel_is_present = False
            # In case of Rule 2, where a word starts with a consonant sound
            for index, letter in enumerate(word):
                if letter in VOWEL_SOUND:
                    result.append(word[index:] + word[:index] + suffix)
                    vowel_is_present = True
                    break  # Break after vowel is spotted, because we only need to spot one first vowel

            # In case of Rule 4, where a word starts with a consonant sound AND also has no vowel,
            # but it has a 'y' after a consonant (which make it becomes a vowel-sound)
            if "y" in word and not vowel_is_present and word.index("y") != 0:
                y_index = word.index("y")
                result.append(word[y_index:] + word[:y_index] + suffix)

    return " ".join(result)
