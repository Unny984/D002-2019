import random
print("Welcome to the rock-paper-scissor!\nYou are going to play against a minion!")
print("""
1.                 2.                           3.
    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)
""")
f = input("Please input your choice\n")
if f == 1:
    print("You choose rock")
elif f == 2:
    print("You choose paper")
elif f == 3:
    print("You choose scissor")

m = random.randint(1,3)
print(m)
if m == 1:
    print("Minion choose rock")
elif m == 2:
    print("Minion choose paper")
elif m == 3:
    print("minion choose scissor")

if f == 1 and m == 1:
    print("Draw!")
elif f == 1 and m == 2:
    print("You lose!")
elif f == 1 and m == 3:
    print("You win!")
elif f == 2 and m == 1:
    print("You win!")
elif f == 2 and m == 2:
    print("Draw!")
elif f == 2 and m == 3:
    print("You lose!")
elif f == 3 and m == 1:
    print("You lose!")
elif f == 3 and m == 2:
    print("You win!")
elif f == 3 and m == 3:
    print("Draw!")
