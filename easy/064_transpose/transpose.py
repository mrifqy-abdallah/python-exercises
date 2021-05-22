from itertools import zip_longest

def transpose(lines: str) -> str:
    if not lines:
        return ""

    mark = chr(191)  # is '¿' in unicode
    lines = zip_longest(*lines.splitlines(), fillvalue=mark)
    
    return "\n".join(map(lambda x: "".join(x).rstrip(mark).replace(mark, " "), lines))