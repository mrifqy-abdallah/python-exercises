def recite(start_verse: int, end_verse: int) -> 'list[str]':
    result = []
    for i in range(start_verse, end_verse + 1):
        result.append(the_song(i))
    return result


def the_song(verse_index: int) -> str:
    SONG_DICT = {
        1: "the house that Jack built.",
        2: "the malt that lay in",
        3: "the rat that ate",
        4: "the cat that killed",
        5: "the dog that worried",
        6: "the cow with the crumpled horn that tossed",
        7: "the maiden all forlorn that milked",
        8: "the man all tattered and torn that kissed",
        9: "the priest all shaven and shorn that married",
        10: "the rooster that crowed in the morn that woke",
        11: "the farmer sowing his corn that kept",
        12: "the horse and the hound and the horn that belonged to"
    }

    whole_verse = ["This is"]

    for i in range(verse_index, 0, -1):
        whole_verse.append(SONG_DICT[i])
    return " ".join(whole_verse)