import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["Cake" , "Guitar" , "Pen"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder+="_ "
print(placeholder)

game_over = False

correct_letters = []

while not game_over:

    guess = input("\nGuess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display+=" _ "
    print(display)
    if "_" not in display:
        game_over = True
        print("You win!")