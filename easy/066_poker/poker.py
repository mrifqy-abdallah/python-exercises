CARDS_VALUE = "  23456789TJQKA"


def best_hands(hands: 'list[str]') -> 'list[str]':
    if not hands:
        return None

    scores = [count_score(hand) for hand in hands]
    max_score = max(scores)
    return [hand for score, hand in zip(scores, hands) if score == max_score]


def count_score(hand: str) -> tuple:

    # Take an example of a `hand` input of "4S AH AS 7C AD"

    # First we map the value of each card
    # At this phase, the card's type is ignored because the card's type is only used to check if it's a flush
    # Code below will results in: [4, 14, 14, 7, 14]
    kinds = [CARDS_VALUE.index(r) for r, _ in hand.replace("10", "T").split()]

    # Then map the amount of different cards and its value, and store it descendingly
    # `counts` and `cards_value` below will results in (3, 1, 1) and (14, 7, 4), respectively
    counts, cards_value = zip(*sorted(((kinds.count(k), k) for k in set(kinds)), reverse=True))

    # Change the value of cards_value in case of a wheel straight
    cards_value = (5, 4, 3, 2, 1) if cards_value == (14, 5, 4, 3, 2) else cards_value 

    straight = len(counts) == 5 and (max(cards_value) - min(cards_value) == 4)
    flush = len(set(c[-1] for c  in hand.split())) == 1

    # Finally, find its score
    # Example above will have a score of '3'
    score = (
        9 if counts == 5 else           # Five of a kind
        8 if straight and flush else    # Straight flush
        7 if counts == (4, 1) else      # Four of a kind
        6 if counts == (3, 2) else      # Full house
        5 if flush else
        4 if straight else
        3 if counts[0] == 3 else
        2 if counts[:2] == (2, 2) else
        1 if counts[0] == 2 else
        0
    )

    # Return the score and the cards_value as one tuple in lexicographic order
    # So the returned value of the example above will be: (3, 14, 7, 4)
    return score, *cards_value