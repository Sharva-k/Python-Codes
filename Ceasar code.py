alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True


def ceasar(original_txt,shift_count,encode_or_decode):
    output_txt=""

    for letter in original_txt:
        
        if letter not in alphabet:
            output_txt+=letter
        else:
            if encode_or_decode == "decode":
                shift_count*=-1

            shifted_position = alphabet.index(letter)+shift_count
            shifted_position%=len(alphabet)
            output_txt+=alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_txt}")

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text,shift,direction)

    restart  = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("BYE!")