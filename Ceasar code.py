alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(original_txt , shift_count):
#     cipher_txt =""
#     for letter in original_txt:
#         shifted_position = alphabet.index(letter) + shift_count
#         shifted_position%=len(alphabet)

#         cipher_txt+=alphabet[shifted_position]

#     print(f"Here is the encoded message:{cipher_txt}")
# encrypt(original_txt=text,shift_count=shift)



def decrypt(original_txt,shift_count):
    output_txt=""
    for letter in original_txt:
        shifted_position = alphabet.index(letter)-shift_count
        shifted_position%=len(alphabet)
        output_txt+=alphabet[shifted_position]
    print(f"Here is the decoded msg:{output_txt}")
decrypt(original_txt=text,shift_count=shift)