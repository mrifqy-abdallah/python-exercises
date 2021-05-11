from itertools import islice
from functools import reduce


def largest_product(series: str, size: int):
    if size == 0:
        return 1

    if not series.isdigit() or size > len(series) or size < 0:
        raise ValueError("Size cannot less than zero AND must be equal or less than series' length")

    generate_series = (islice(series, i, None) for i in range(size))
    # For a series like "9184939" and a length of 3, the result will be
    # ( ['9', '1', '8', '4', '9', '3', '9'],
    #   ['1', '8', '4', '9', '3', '9'],
    #   ['8', '4', '9', '3', '9']  )
    # Note that the datatype is generator

    # And then we unzip it
    generate_series = zip(*generate_series)
    # It'll be resulting in zip object with value
    # ('9', '1', '8'), ('1', '8', '4'), ('8', '4', '9'), ('4', '9', '3'), ('9', '3', '9')

    # Two lines above is taken from ../029_series/series.py

    # Then turn values inside generate_series to int
    result = ((int(j) for j in i) for i in generate_series)

    largest_serial = 0
    
    for serial in result:
        serial_multiplied = reduce((lambda x,y: x*y), serial)  # Count the sum of multiplication of the serial
        if serial_multiplied > largest_serial:
            largest_serial = serial_multiplied

    return largest_serial
