# “Break and continue statements are used to alter the flow or normal working of a loop, 
# that could be either a “for loop” or “while loop”.
i = 0
while(True):
    if i + 1 < 5:
        i = i + 1
        continue
    print(i, end=" ")
    if(i == 40):
        break # Stops the Loop
    i = i + 1

# Quizz
print("\n*** Quizz ***")
while(True):
    inp = int (input("Enter your Number\n"))
    if inp > 100:
        print("Congrats, you have entered a number grater than 100\n")
        break
    else:
        print("Please try again\n")
        continue