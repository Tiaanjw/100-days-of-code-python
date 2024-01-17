import string

alphabet = list(string.ascii_lowercase)

def calculate_shifted_index(alphabet_length, current_index, shift, encdec):
    if encdec == 'encode':
        if current_index + shift > alphabet_length:
            return current_index + shift - alphabet_length
        else:
            return current_index + shift
    else:
        return current_index - shift


def encrypt(text, shift):
    alphabet_length = len(alphabet)
    encrypted_str = ""
    
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted_str += alphabet[calculate_shifted_index(alphabet_length, index, shift, 'encode')]
        else:
            encrypted_str += letter
    
    return encrypted_str

def decrypt(text, shift):
    alphabet_length = len(alphabet)
    decrypted_str = ""
    
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            decrypted_str += alphabet[calculate_shifted_index(alphabet_length, index, shift, 'decode')]
        else:
            decrypted_str += letter
    
    return decrypted_str

end_program = False
while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        print(encrypt(text, shift))
    else:
        print(decrypt(text, shift))
    
    another = input("Would you like to try again? ('yes' or 'no'): ")
    if another == "no": 
        end_program = True