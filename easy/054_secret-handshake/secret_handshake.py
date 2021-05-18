def commands(number: int):
    result = []
    binary = int(format(number, "b"))

    # The instruction is asking to check the binary backwards
    # Here the checking is forward, therefore the result needs to be reversed by default
    reverse = True

    while binary > 0:
        if binary >= 10000:
            reverse = False
            binary %= 10000
        elif binary >= 1000:
            result.append("jump")
            binary %= 1000
        elif binary >= 100:
            result.append("close your eyes")
            binary %= 100
        elif binary >= 10:
            result.append("double blink")
            binary %= 10
        elif binary == 1:
            result.append("wink")
            binary %= 1
    
    if reverse:
        result.reverse()

    return result