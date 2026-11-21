secret_number = 89
guess = int(input("Guess the secret number between 1 and 100: "))

while guess != secret_number:

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    guess = int(input("Try again: "))

print("Congratulations! You passed it. ")