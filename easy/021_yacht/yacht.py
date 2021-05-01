from statistics import mode

"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

check_dices_category = {
    "YACHT" : lambda x: len(set(x)) == 1,  # All 5 dices has one same number
    "ONES" : lambda x: 1 in x, 
    "TWOS" : lambda x: 2 in x,
    "THREES" : lambda x: 3 in x,
    "FOURS" : lambda x: 4 in x,
    "FIVES" : lambda x: 5 in x,
    "SIXES" : lambda x: 6 in x,
    "FULL_HOUSE" : lambda x: {x.count(i) for i in set(x)}.issubset({2,3}),  # 5 dices has 2 same numbers AND 3 same numbers
    "FOUR_OF_A_KIND" : lambda x:  [i for i in set(x) if x.count(i) >= 4],  # At least 4 out of 5 dices has same number
    "LITTLE_STRAIGHT" : lambda x: sorted(x) == [1, 2, 3, 4, 5],  # 5 dices shows 1-5 
    "BIG_STRAIGHT" : lambda x: sorted(x) == [2, 3, 4, 5, 6],  # 5 dices shows 2-6
    "CHOICE" : lambda x: True  
}

count_scores_category = {
    "YACHT" : lambda x: 50,
    "ONES" : lambda x: x.count(1) * 1,
    "TWOS" : lambda x: x.count(2) * 2,
    "THREES" : lambda x: x.count(3) * 3,
    "FOURS" : lambda x: x.count(4) * 4,
    "FIVES" : lambda x: x.count(5) * 5,
    "SIXES" : lambda x: x.count(6) * 6,
    "FULL_HOUSE" : lambda x: sum(x),
    "FOUR_OF_A_KIND" : lambda x: mode(x) * 4,
    "LITTLE_STRAIGHT" : lambda x: 30,
    "BIG_STRAIGHT" : lambda x: 30,
    "CHOICE" : lambda x: sum(x)
}


def score(dice, category):
    score = 0
    # Is True if the dice match the category
    if check_dices_category[category](dice):
        score = count_scores_category[category](dice)
    return score
