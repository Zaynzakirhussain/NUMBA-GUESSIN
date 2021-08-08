import random

gnumber = random.randint(0,9)
chances = 2
daGame = "Number Game"
guess = "Guess a number from 0 to 9"
scare = "And you only get TWO chance"

print(daGame)
print(guess)
print(scare)

number = int(input("Enter the answer: "))

if(gnumber > number):
    tlose = "The number is bigger..."
    print(tlose)
    chances = chances - 1

if(gnumber < number):
    tlose = "The number is smaller..."
    print(tlose)
    chances = chances - 1

if(gnumber == number):
    win = "You Win!!! Congratulations..."
    print(win)

if(chances == 0):
    lose = "You lose... HA LOSER!!!"
    print(lose)

if(gnumber != number):
    number = int(input("Enter the answer: "))

    if(gnumber > number):
        tlose = "The number is bigger..."
        print(tlose)
        chances = chances - 1

    if(gnumber < number):
        tlose = "The number is smaller..."
        print(tlose)
        chances = chances - 1

    if(gnumber == number):
        win = "You Win!!! Congratulations..."
        print(win)

    if(chances == 0):
        lose = "You lose... HA LOSER!!!"
        print(lose)
