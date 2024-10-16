import random

lower = int(input("Enter lower limit: "))
higher = int(input("Enter higher limit (not more than 300): "))

if higher > 300:
    print("Out of range!!!")
    exit()

if higher - lower <= 100:
    chances = 3
    print("You have 3 chances to guess.")
elif (higher - lower <= 200) and (higher - lower > 100):
    chances = 5
    print("You have 5 chances to guess.")
else:
    chances = 10
    print("You have 10 chances to guess.")

secret_number = random.randint(lower, higher)
print("I have picked a number in my mind. Your turn!!!")
print(f"Guess the number between {lower} and {higher}.")

count = 0

while count < chances:
    user_guess = int(input("Enter your guess: "))
    
    if user_guess < lower or user_guess > higher:
        print("Guess a valid number.")
        continue  # Skip to the next iteration of the loop
    
    count += 1  # Increment count for each guess
    
    if user_guess == secret_number:
        print(f"You won in {count} attempts!")
        print(f"The secret number was {secret_number}")
        break  # Exit the loop if the guess is correct
    else:
        difference = abs(user_guess - secret_number)
        if difference <= 10:
            print("with the proximity of 10")
        elif difference <=20:
            print("with the proximity of 20")
        elif difference <=50:
            print("with the proximity of 50")
        else:
            print("TOO FAR")
        

if count == chances and user_guess != secret_number:
    print(f"You lost! The secret number was {secret_number}.")