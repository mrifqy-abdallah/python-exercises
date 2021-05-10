from itertools import islice

def slices(series: str, length: int):
    result = []

    if not series or length > len(series) or length < 1:
        raise ValueError("Series cannot be empty AND slice length must be more than 0 but less or equal than the series' length")
    
    generate_series = (islice(series, i, None) for i in range(length))
    # For a series like "9184939" and a length of 3, the result will be
    # ( ['9', '1', '8', '4', '9', '3', '9'],
    #   ['1', '8', '4', '9', '3', '9'],
    #   ['8', '4', '9', '3', '9']  )
    # Note that the datatype is generator

    # And then we unzip it
    generate_series = zip(*generate_series)
    # It'll be resulting in zip object with value
    # ('9', '1', '8'), ('1', '8', '4'), ('8', '4', '9'), ('4', '9', '3'), ('9', '3', '9')
    
    # If you are debugging and want to see the value of generate_series using print,
    # you need to assign generate_series to a new variable first.
    # If you dont, generate_series below will be empty. 
    # Find out about generator and zip iterator if you're unfamiliar about this.
    
    for i in generate_series:
        result.append(''.join(i))

    return result
