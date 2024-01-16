import string
import random

alphabet_list = list(string.ascii_letters)
number_list   = ['0','1','2','3','4','5','6','7','8','9']
symbol_list   = ['!','#','$','%','&','(',')','*','+']

nr_letters = int(input("How many characters do you want? "))
nr_number  = int(input("How many numbers do you want? "))
nr_symbols = int(input("How many symbols do you want? "))

selected_letters = []
selected_number = []
selected_symbols = []

for idx in range(0, nr_letters):
  selected_letters.append(random.choice(alphabet_list))

for idx in range(0, nr_number):
  selected_number.append(random.choice(number_list))

for idx in range(0, nr_symbols):
  selected_symbols.append(random.choice(symbol_list))

complete_list = selected_letters + selected_number + selected_symbols
random.shuffle(complete_list)
password = "".join(complete_list)

print(f"Your password is {password}")