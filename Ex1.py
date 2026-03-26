import pathlib  # yes, for real lol
import typing


def count_lines(filepath: pathlib.Path) -> int | None:
    line_cnt = 0
    if not filepath.exists():
        return None
    else:
        file = filepath.open()
        for line in file:
            if len(line.strip()) != 0:
                line_cnt = line_cnt + 1
        return line_cnt



def find_occurences(needle: str, file: typing.TextIO)