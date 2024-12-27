import random

# Print multiline instruction
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      'Rock vs Paper -> Paper wins\n'
      'Rock vs Scissors -> Rock wins\n'
      'Paper vs Scissors -> Scissors wins\n')

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n") 

    # Validate input to ensure it's a number and within range
    try:
        choice = int(input("Enter your choice (1/2/3): "))
        while choice > 3 or choice < 1:
            choice = int(input('Enter a valid choice please (1/2/3): '))
    except ValueError:
        print("Invalid input. Please enter a number (1, 2, or 3).")
        continue

    # Map the user's choice to its name
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # Print user choice
    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")

    # Computer chooses randomly among 1, 2, and 3
    comp_choice = random.randint(1, 3)

    # Map the computer's choice to its name
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    # Determine the winner
    if choice == comp_choice:
        print("<== It's a tie! ==>")
    elif (choice == 1 and comp_choice == 3) or \
         (choice == 2 and comp_choice == 1) or \
         (choice == 3 and comp_choice == 2):
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    # Ask if the user wants to play again
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

# After exiting the while loop, print thanks for playing
print("Thanks for playing!")
