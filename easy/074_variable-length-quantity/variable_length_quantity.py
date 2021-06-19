def encode(numbers: 'list[int]') -> 'list[int]':
    result = []
    for n in numbers:
    	build_number = [n % 128]
    	n = n // 128
    	while n > 0:
    		build_number.append(n % 128 + 128)
    		n = n // 128
    	build_number.reverse()
    	for r in build_number:
    		result.append(r)
    return result


def decode(bytes_: 'list[int]') -> 'list[int]':
    result = []
    build_number = 0
    for by in bytes_:
    	build_number = build_number * 128 + by % 128
    	if by < 128:
    		result.append(build_number)
    		build_number = 0
    if by > 127:
    	raise ValueError("Number not properly terminated")
    return result