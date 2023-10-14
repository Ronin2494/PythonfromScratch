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

print(rock)
print(paper)
print(scissors)

user_choice = int(input("What do you want to chose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice == 0:
  print("You chose rock", rock)
elif user_choice == 1:
  print("You chose paper", paper)
elif user_choice == 2:
  print("You chose scissors", scissors)
else:
  print("Invalid choice")

computer_choice = random.randint(0,2)
if computer_choice == 0:
  print("Computer chose rock", rock)
elif computer_choice == 1:
  print("Computer chose paper", paper)
elif computer_choice == 2:
  print("Computer chose scissors", scissors)

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