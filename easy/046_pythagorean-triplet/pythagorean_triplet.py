def triplets_with_sum(number: int):
    result = []  
    for x in range(1, number//3):
        for y in range(x+1, number//2):
            z = number - x - y
            if x**2 + y**2 == z**2:
                result.append([x, y, z])
    return result

    # Testing it with number = 30.000 takes time for about 2 minutes and half
