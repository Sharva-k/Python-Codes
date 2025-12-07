import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,scissors,paper]
user_choice = int(input("What do you chose ? Type 0 for rock , 1 for scissors , 2 for paper: "))
if user_choice>=0 or user_choice<3:
    print("You chose:")
    if user_choice == 0:
        print("rock")
    elif user_choice == 1:
        print("scissors")
    else:
        print("paper")
    print(game_images[user_choice])
comp_choice = random.randint(0,2)

print(f"Computer chose:")
print(game_images[comp_choice])

if user_choice>=3 or user_choice<0:
    print("You types invalid number")
elif user_choice == 0 and comp_choice == 2:
    print("You lose")
elif user_choice == 2 and comp_choice == 0:
    print("You win")
elif user_choice > comp_choice:
    print("You lose")
elif comp_choice > user_choice:
    print("You win")
elif user_choice == comp_choice:
    print("Draw")
