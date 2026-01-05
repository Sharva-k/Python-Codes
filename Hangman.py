import random
word_list = ["Cake" , "Guitar" , "Pen"]
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right!")
    else:
        print("Wrong!")
     