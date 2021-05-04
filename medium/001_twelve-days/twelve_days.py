def recite(start_verse: int, end_verse: int):
    result = []
    for i in range(start_verse, end_verse + 1):
        result.append(collect_verse(i))
    return result


def collect_verse(verse_index):
    main_verse = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, and ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ]

    days = {
        1: "first", 
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }

    whole_verse = "On the " + days[verse_index] + " day of Christmas my true love gave to me: "
    for i in range(verse_index, 0, -1):
        whole_verse += main_verse[i-1]
    return whole_verse
