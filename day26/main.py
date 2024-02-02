import pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (idx, row) in nato_alphabet_data.iterrows()}
# print(nato_alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
nato_words = [nato_alphabet_dict[letter] for letter in user_input]
print(nato_words)
