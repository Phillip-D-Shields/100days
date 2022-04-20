# basic way to open file, needs to manually be closed
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# auto closes file after usage
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# "w" - write mode, erase everything and rewrite with new text
with open("my_file.txt", mode="w") as file:
    file.write("Hello World")

# "a" - append mode, add text to end of file
with open("my_file.txt", mode="a") as file:
    file.write("\nKiaora Team")

# "w" - on a non existent file creates it as a new file
with open("my_second_file.txt", mode="w") as file:
    file.write("magic!")