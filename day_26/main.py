# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

nato_file = pandas.read_csv('./nato_phonetic_alphabet.csv')

word_dict = {row.letter.upper(): row.code for (index, row) in nato_file.iterrows()}

user_input = input('Enter a word: ').upper()

result = [word_dict[letter] for letter in user_input]

print(result)
