def recite(start: int, take: int=1):
    lyrics = []
    count_beers = 0
    while count_beers < take:
        lyrics.extend(repeat_lyrics(start))
        count_beers += 1
        start -= 1
    # Delete empty string ("") from the last element
    lyrics.pop()
    return lyrics


def repeat_lyrics(number: int):
    count1 = count_bottle(number)
    count2 = count_bottle(number-1)
    take = take_bottle(number)
    the_lyric = [
        f"{count1} of beer on the wall, {count1} of beer.".capitalize(),
        f"{take}, {count2} of beer on the wall.",
        ""
        ]
    return the_lyric


def count_bottle(x):
    if x > 1:
        return f"{x} bottles"
    elif x == 1:
        return f"1 bottle"
    elif x == 0: 
        return "no more bottles"
    elif x < 1:
        return "99 bottles"


def take_bottle(x):
    if x > 1:
        return "Take one down and pass it around"
    elif x == 1:
        return "Take it down and pass it around"
    else:
        return "Go to the store and buy some more"