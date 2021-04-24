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

choice=int(input("Choose 0 for rock 1 for paper and 2 for scissors :"))

game=[rock,paper,scissors]
#outcome=[won,lose,draw]
print(game[choice])
import random
output=random.randint(0,2)
print("computer chooses")
print(game[output])
if (choice==2 and output==0) or (choice==0 and output==1)or (choice== 1 and output==2):
  print("You lose")
elif(choice==0 and output==2) or (choice==1 and output==0)or (choice== 2 and output==1):
  print("You win")
else:
  print("Its a draw")