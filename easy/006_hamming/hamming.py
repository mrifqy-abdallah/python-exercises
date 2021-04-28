def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The two DNAs has different length!")
    if strand_a == strand_b:
        return 0
    else:
        distance = 0
        for i, char in enumerate(strand_a):
            if char != strand_b[i]:
                distance += 1
        return distance
