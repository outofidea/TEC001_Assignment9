import pathlib
import typing
def find_occurences(needle: str, file_path: pathlib.Path) -> list[int]:
    file = open(file_path)
    occurrences = []
    for (idx, line) in enumerate(file):
        if needle in line:
            occurrences.append(idx + 1)
    return occurrences


print(find_occurences("Alex", pathlib.Path("sample_data/scores.txt")))