import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# print(phonetic_dict)

user_input = input("enter a word to encode: ").upper()

return_code = [phonetic_dict[letter] for letter in user_input]

print(return_code)
