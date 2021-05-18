def commands(number: int):
    handshakes = ["wink", "double blink", "close your eyes", "jump"]
    result = [handshake for i, handshake in enumerate(handshakes) if 2**i & number]

    if 2**4 & number:
        result.reverse()
    return result
