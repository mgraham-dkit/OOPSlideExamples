from random import randint

keep_playing = True
max_guesses = 5
min_value = 1
max_value = 100
win_lose = {}
while keep_playing:
    guesses = []
    choice = input("Do you want to play a guessing game? (Y/N)\n")
    match choice.lower():
        case "y":
            print("Great, let's go!")
        case "n":
            print("Ok, see you later")
            keep_playing = False
            continue
        case _:
            print("Please choose Y or N")
            continue

    value = randint(min_value, max_value)
    winner = False

    while len(guesses) < max_guesses and not winner:
        try:
            guess = int(input(f"Please guess a number between {min_value} and {max_value}: "))
            guesses.append(guess)

            if guess == value:
                print("Congratulations!")
                winner = True
        except Exception as e:
            print(f"An exception occurred: {e}")
            print("Please enter a number using only digits")

    print(f"The number was {value}")
    print(f"You guessed {guesses}")