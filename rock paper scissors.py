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

a = input("What will you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: ")
p = random.choice(["0", "1", "2"])

if a == "0":
    print(rock)
elif a == "1":
    print(paper)
elif a == "2":
    print(scissors)
print("The computer chose ",p)
if p == "0":
    print(rock)
elif p == "1":
    print(paper)
elif p == "2":
    print(scissors)

if a == "0" and p == "1":
    print("You lose")
if a == "1" and p == "0":
    print("You win!")
if a == "1" and p == "2":
    print("You lose")
if a == "2" and p == "1":
    print("You win!")
if a == "0" and p == "2":
    print("You win!")
if a == "2" and p == "0":
    print("You lose")
if a == "0" and p == "0" or a == "1" and p == "1" or a == "2" and p == "2":
    print("It's a tie")
