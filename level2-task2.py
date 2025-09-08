import random

a,b=map(int, input("Enter the range (2 numbers seperated by a space) : ").split())
random_num=random.randint(a,b)

while(True):
    user_num=int(input("Enter the number you think is the random number: "))
    if user_num < random_num:
        print("Your guess is low.")
    elif user_num>random_num:
        print("Your guess is high.")
    if user_num==random_num:
        break
print(f"You guessed the number!: {random_num}")

