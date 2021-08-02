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

variables = [rock, paper, scissors]

you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

import random
computer = random.randint(0,2)

if you==2 and computer==0:
  print("You chose")
  print(variables[you])
  print("Computer chose")
  print(variables[computer])
  print("Computer wins.")
elif you==0 and computer==2:
  print("You chose")
  print(variables[you])
  print("Computer chose")
  print(variables[computer])
  print("You wins.")
elif computer>you:
  print("You chose")
  print(variables[you])
  print("Computer chose")
  print(variables[computer])
  print("Computer wins.")
elif you==computer:
  print("You chose")
  print(variables[you])
  print("Computer chose")
  print(variables[computer])
  print("It's a draw.")
else:
  print("You chose")
  print(variables[you])
  print("Computer chose")
  print(variables[computer])
  print("You win.")