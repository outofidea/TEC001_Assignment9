def caesar_xform(char_in: str, shift_nr: int, shift_dir: bool) -> str:
                
                shifts = shift_nr if shift_dir else shift_nr * -1

                char_pos_ascii = ord(char_in)
                char_case = char_in.isupper()

                if(char_case):
                    return chr((char_pos_ascii + shifts)% (26 + 65))
                else:
                    return chr((char_pos_ascii + shifts)% (26 + 97))





def caesar(filename: str, nr_shifts: int, shift_dir: bool):

    out_file = open("cipher.txt", "w")

    line = ""
    for line in open(filename):
        xform_word = ""
        for word in line.split():
            for char in word:
                if char.isalpha():
                    xform_word += caesar_xform(char, nr_shifts, shift_dir)
            line += f"{xform_word} "

        out_file.write(line + "\n")
    
    out_file.close()



caesar("sample_data/clear.txt", 3, False)







            