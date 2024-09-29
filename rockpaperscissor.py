import random

options=["Rock", "Paper", "Scissors"]
computer=random.choice(options)
user=input("Enter your choice 'Rock' 'Paper' or 'Scissors' :\n")
if user==computer:
    print('Its a TIE')
elif user=='Rock':
    if computer=='Paper':
        print('YOU WON!!!')
    else:
        print('YOU LOST!!!')
elif user=='Paper':
    if computer=='Rock':
        print('YOU WON!!!')
    else:
        print('YOU LOST!!!')
elif  user=='Scissors':
    if computer=='Paper':
        print('YOU WON!!!')
    else:
        print('YOU LOST!!!')
else:
    print("Invalid choice !!!!!!!")
