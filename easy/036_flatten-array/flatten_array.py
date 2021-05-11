def flatten(iterable: list):
    _flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
    # There are many available methods from python modules to flatten a list, but we're not using any of them.
    # Methods such as itertools.chain.from_iterable, sum(list, []), etc is ONLY capable to handle nested list.
    # What I mean by that is those methods aren't capable to flatten a list like this one
    #       [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
    # which has int (or any other datatype) value(s) outside the nest.

    result = _flatten(iterable)
    while None in result:
        result.remove(None)
    return result
