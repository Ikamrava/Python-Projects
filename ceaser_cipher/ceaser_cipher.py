import art

print(art.logo)
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
            
    for letter in start_text:
        if letter not in art.alphabet:
            end_text += letter
        else:
            possition = art.alphabet.index(letter)
            new_possition = possition + shift_amount
            end_text += art.alphabet[new_possition]
            
    print(f"The {cipher_direction}d text is {end_text}")



should_continue = True

while should_continue:
    directin = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
       shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=directin)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    if restart == "no":
        should_continue = False
        print("Goodbye")

            




