# Number Guessing Game

# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while(number_of_guesses<=9):
    guess_number = int(input("Guess the number:"))
    if guess_number < 18:
        print("you enter less number please input greater number.")
    elif guess_number > 18:
        print("you enter greater number please input smaller number.")
    else:
        print("You won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")