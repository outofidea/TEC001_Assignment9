def find_occurences(needle: str, file: typing.TextIO) -> list[int]:
    occurrences = []
    for (idx, line) in enumerate(file):
        if needle in line:
            occurrences.append(idx + 1)
    return occurrences

