import random
word_list = ["Cake" , "Guitar" , "Pen"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder+="_ "
print(placeholder)

guess = input("\nGuess a letter: ").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display+=letter
    else:
        display+=" _ "
print(display)
     