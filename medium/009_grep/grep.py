FLAGS = ["-n", "-l", "-i", "-v", "-x"]
"""
-n : Print the line numbers of each matching line.
-l : Print only the names of files that contain at least one matching line.
-i : Match line using a case-insensitive comparison.
-v : Invert the program -- collect all lines that fail to match the pattern.
-x : Match one line entirely, not just if the line contain a match.
"""


def grep(pattern: str, flags: str, files: 'list[str]') -> str:
    flags = flags.split()
    match_result = []
    ignore_case = False

    if not all(map(lambda x: x in FLAGS and flags.count(x) == 1, flags)):
        raise ValueError("Invalid flag(s)")

    if "-i" in flags:
        pattern = pattern.lower()
        ignore_case = True

    for file in files:
        with open(file, "r") as f:
            for index, line in enumerate(f.readlines()):
                metaline = line
                if ignore_case:
                    metaline = metaline.lower()

                # '-v' and '-x' flags need to be checked inclusively
                if "-v" in flags and "-x" in flags:
                    match = pattern + "\n" != metaline
                elif "-v" in flags and "-x" not in flags:
                    match = pattern not in metaline
                elif "-v" not in flags and "-x" in flags:
                    match = pattern + "\n" == metaline
                else:
                    match = pattern in metaline
                
                if match:
                    if "-l" in flags:
                        match_result.append(file)
                        break
                    # If the file in `files` is more than one, filename should be included in the matched line
                    elif "-n" in flags:
                        if len(files) > 1:
                            match_result.append(f"{file}:{index + 1}:{line}")
                        else:
                            match_result.append(f"{index + 1}:{line}")
                    else:
                        if len(files) > 1:
                            match_result.append(f"{file}:{line}")
                        else:
                            match_result.append(line)

    if not match_result:
        return ""

    # '-l' flag return filenames, therefore a separator for each filename is needed
    if "-l" in flags:
        return "\n".join(match_result) + "\n"

    return "".join(match_result)