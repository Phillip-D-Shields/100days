PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
    print(names)

with open("./input/Letters/starting_letter.txt", "r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open("./output/ReadyToSend/{}.txt".format(stripped_name), mode="w") as new_letter_file:
            new_letter_file.write(new_letter)