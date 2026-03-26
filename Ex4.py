# seems like i was right with this approach (i deleted this once)

# basically we normalize the ascii pos to alphabet pos and then convert it to ascii pos again


lwr_case_offset = 97
upr_case_offset = 65

lwr_upr_case_offset = lwr_case_offset - upr_case_offset


def caesar_xform(char_in: str, shift_nr: int, shift_dir: bool) -> str:

    shifts = shift_nr if shift_dir else shift_nr * -1

    char_pos_ascii = ord(char_in)
    char_case = char_in.isupper()

    char_idx_alpha = char_pos_ascii - lwr_case_offset

    if char_idx_alpha < 0:
        char_idx_alpha = char_idx_alpha + lwr_upr_case_offset

    print(f"Char: {char_in}, ASCII pos: {char_pos_ascii}, alpha idx: {char_idx_alpha}")
    if char_case:
        char = chr(((char_idx_alpha + shifts) % 26) + upr_case_offset)
        print(f"xformed char: {char}")
        return char
    else:
        char = chr(((char_idx_alpha + shifts) % 26) + lwr_case_offset)
        print(f"xformed char: {char}")
        return char


def caesar(filename: str, nr_shifts: int, shift_dir: bool):

    out_file = open("cipher.txt", "w")

    for line in open(filename):
        xform_line = ""
        for word in line.split():
            xform_word = ""
            for char in word:
                if char.isalpha():
                    xform_word += caesar_xform(char, nr_shifts, shift_dir)
                else:
                    xform_word += char
            xform_line += f"{xform_word} "

        out_file.write(xform_line + "\n")

    out_file.close()


caesar("sample_data/clear.txt", 3, False)
