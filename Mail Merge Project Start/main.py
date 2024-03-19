with open("./Input/Letters/starting_letter.txt") as file:
    contents = file.readlines()
    contents = " ".join(map(str, contents))
    contents.strip().split()


with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    for name in names:
        name_clear = name.strip("\n")
        new_letter = contents.replace("[name]",name_clear)
        with open(f"./Output/ReadyToSend/letter_for_{name_clear}.txt",mode="w") as end_file:
            end_file.write(new_letter)



