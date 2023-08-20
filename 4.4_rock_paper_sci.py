
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

#Write your code below this line 👇

import random
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("Invalid number, you lose!")
else:
    print(game_images[user_choice])
    ai_move = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[ai_move])


    if user_choice == 0 and ai_move ==2:
        print("You win!")
    elif ai_move == 0 and user_choice == 2:
        print("You lose!")
    elif ai_move > user_choice:
        print("You lose!")
    elif user_choice > ai_move:
        print("You lose!")
    elif user_choice == ai_move:
        print("It's a draw")