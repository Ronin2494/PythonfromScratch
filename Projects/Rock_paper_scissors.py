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

user_choice = int(input("What do you want to chose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(f"You chose {game_images[user_choice]}\n")

### Now computer will chose randomly####
computer_choice = random.randint(0,2)
print(f"Computer chose {game_images[computer_choice]}\n")

if user_choice == computer_choice:
  print("It's a draw!")
elif user_choice == 0 and computer_choice == 1:
  print("You lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif user_choice == 1 and computer_choice == 0:
  print("You win!")
elif user_choice == 1 and computer_choice == 2:
  print("You lose!")
elif user_choice == 2 and computer_choice == 0:
  print("You lose!")
elif user_choice == 2 and computer_choice == 1:
  print("You win!")
else:
  print("Invalid choice from user")