#import ascii_art
import random

#print(ascii_art.logo)
#To do list

#TODO 1 - Check that the player entered 5 things

#TODO 2 - Convert the strings into integers

#TODO 3 - Check that the numbers are between 1 and 69

#TODO 4 - Check that the numbers are unique

while True:
    print("enter 5 number between 1 to 69")
    response = input(">")

    numbers = response.split()
#Check that the player entered 5 things
    if len(numbers)!=5:
        print("enter 5 numbers seprated by space")
        continue
#Convert the strings into integers
    try:
        for i in range(5):
            numbers[i]= int(numbers[i])
    except ValueError:
        print("Please enter numbers not sentense ")
        continue
#Check that the numbers are between 1 and 69
    between_1_69 = True
 
    for i in numbers:
        if not(1<= i <=69):
            print("please enter numbers between 1 and 69")
            between_1_69 = False
            break
    if not between_1_69:
        continue

    if len(set(numbers)) !=5:
        print("You must enter unique number ")
        continue
    break

#Step 2 - Ask the player to select the powerball between 1 to 26


#TODO 1 - Convert the strings into integers

#TODO 2 - Check that the number is between 1 and 26

while True:
    print("Please enter the powerball between 1 to 26")
    response=input('> ')

    try:
        powerball = int(response)
    except ValueError:
        print("please enter number not char \n")
        continue
    if not(1 <= powerball <=26):
        print("The powerball number must be between 1 and 26")
        continue
    break

#Step 3 - Enter the number of times you want to play

#TODO 1 - Convert the strings into integers
#TODO 2 - Check that the number is between 1 and 1000000

while True:

    print("How many time you want to try? \n(max:100)")
    response=input('> ')
    try:
        numPlays = int(response)
    except ValueError:
        print(" Please enter a number not character \n")
        continue
    if not(1<= numPlays <= 100):
        print(" you can try max 100 time")
        continue
    break
        

#Step 4 - Run the simulation

#TODO 1 - Come up with lottery numbers

#TODO 2 - Display winning numbers

#TODO 3 - Check for winner

price = '$' + str(2 * numPlays)
print(f"It costs {price} to play {numPlays} times, but dont \nworry. I'm sure you will win it all back.")
input("Press Enter to start...")
possibleNumbers = list(range(1,70))
for i in range(numPlays):
    # Come up with lottery numbers
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1,26)
    # Display winning numbers
    print("The winning numbers are: ", end="")
    allWinningNumbers = ""
    for num in winningNumbers:
        allWinningNumbers += str(num) + ' '
    allWinningNumbers += "and " + str(winningPowerball)
    print(allWinningNumbers, end = "")
    #  Check for winner
    if (set(numbers) == set(winningNumbers) and powerball == winningPowerball):
        print()
        print("You have won the powerball Lottery! Congratulations.")
        break
    else:
        print(" You Lost.")
print(f"You have wasted {price}")
print("Thanks for playing")
