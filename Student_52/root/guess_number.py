import random
import os

HIGH_SCORE_FILE = 'C.PythonTUT'

def read_high_score():
    if not os.path.exists(HIGH_SCORE_FILE):
        return None
    try:
        with open(HIGH_SCORE_FILE, 'r') as f:
            content = f.read().strip()
            return int(content) if content else None
    except:
        return None

def write_high_score(score):
    with open(HIGH_SCORE_FILE, 'w') as f:
        f.write(str(score))

def play_game():
    target = random.randint(1, 100)
    guesses = 0
    print("I'm thinking of a number between 1 and 100. Try to guess it!")
    while True:
        try:
            guess = int(input("Enter your guess: ").strip())
        except ValueError:
            print("Please enter a valid integer.")
            continue
        guesses += 1
        if guess < target:
            print("Too low.")
        elif guess > target:
            print("Too high.")
        else:
            print(f"Correct! You guessed it in {guesses} guesses.")
            return guesses

def main():
    print("=== Guess the Number ===")
    current_high = read_high_score()
    if current_high is None:
        print("No high score yet. Be the first to set one!")
    else:
        print(f"Current high score (fewest guesses): {current_high}")
    while True:
        guesses = play_game()
        current_high = read_high_score()
        if current_high is None or guesses < current_high:
            print("New high score! Saving...")
            write_high_score(guesses)
        else:
            print("You did not beat the high score this time.")
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()
