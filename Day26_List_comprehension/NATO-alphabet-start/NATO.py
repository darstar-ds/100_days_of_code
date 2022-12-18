import pandas as pd

nato_alphabet = pd.read_csv("./Day26_List_comprehension/NATO-alphabet-start/nato_phonetic_alphabet.csv")

# print(nato_alphabet)

nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

# print(nato_alphabet_dict)

user_name = input("Enter a name: ").upper()

code_list = [nato_alphabet_dict.get(letter) for letter in user_name]

print(code_list)