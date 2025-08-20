import random

print("Hii welcome to number guessing game. \nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low,high)
ch = 7
gc = 0

while gc<ch:
    gc+=1
    guess = int(input("Enter your guess: "))

    if guess == num:
        print(f"Correct! the number is {num}. you guessed it in {gc}")
        break
    elif gc >= ch and guess != num:
        print(f'orry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')