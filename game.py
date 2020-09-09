import random
lst=['s','w','g']
chance=10
no_of_chance=0
user_points=0
computer_points=0
print("*********Snake Water Gun Game**********")
print("s for snake,w for water,g for gun\n")

while no_of_chance<chance:
    user_input=input("Snake,Water,Gun: ")
    random_value=random.choice(lst)

    if user_input==random_value:
        print("Tie Both will get 0 point")

    #if user_input is 's'
    elif user_input=='s' and random_value=='w':
        print(f"Your guess is {user_input} and computer guess is {random_value}")
        print("You won 1point")
        user_points=user_points+1
        print(f"User point is {user_points} and computer point is {computer_points}")
    elif user_input=='s' and random_value=='g':
        print(f"Your guess is {user_input} and computer guess is {random_value}")
        print("Computer won 1point")
        computer_points=computer_points+1
        print(f"User point is {user_points} and computer point is {computer_points}")
    #if user_input is w
    elif user_input=='w' and random_value=='s':
        print(f"Your guess is {user_input} and computer guess is {random_value}")
        print("Computer won 1point")
        computer_points=computer_points+1
        print(f"User point is {user_points} and computer point is {computer_points}")
    elif user_input=='w' and random_value=='g':
        print(f"Your guess is {user_input} and computer guess is {random_value}")
        print("You won 1point")
        user_points=user_points+1
        print(f"User point is {user_points} and computer point is {computer_points}")

    #if user_input is g

    elif user_input=='g' and random_value=='s':
        print(f"Your guess is {user_input} and computer guess is {random_value}")
        print("You won 1point")
        user_points=user_points+1
        print(f"User point is {user_points} and computer point is {computer_points}")
    elif user_input=='g' and random_value=='w':
        print(f"Your guess is {user_input} and computer guess is {random_value}")
        print("Computer won 1point")
        computer_points=computer_points+1
        print(f"User point is {user_points} and computer point is {computer_points}")
    else:
        print("Invalid input.Please enter s for snake,w for water,g for gun ")
    no_of_chance=no_of_chance+1
    print(f"You have {chance-no_of_chance} chance left out of {chance}")
print("Game over")

if user_points>computer_points:
    print("You won the game")
elif user_points<computer_points:
    print("Computer won the game")
else:
    print("game Tied")

print(f"User final points is {user_points} and Computer final points is {computer_points}")


