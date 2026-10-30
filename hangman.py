
import random


def hangman():
    print("=" * 40)
    print("       WELCOME TO HANGMAN")
    print("=" * 40)

    # Enter student name
    student_name = input("Enter student name: ").strip()

    if not student_name:
        student_name = "Student"

    # Add multiple words
    words = ["python", "computer", "coding", "program", "science"]

    print("\nHello,", student_name + "!")
    print("You can add your own words to the game.")

    while True:
        choice = input("Do you want to add a word? (yes/no): ")
        choice = choice.lower().strip()

        if choice == "yes":
            new_word = input("Enter a word: ").strip().lower()

            if new_word.isalpha():
                words.append(new_word)
                print("Word added successfully!")
            else:
                print("Please enter letters only.")

        elif choice == "no":
            break

        else:
            print("Please enter yes or no.")

    # Select a random word
    secret_word = random.choice(words)

    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("\n" + "=" * 40)
    print("Student:", student_name)
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect guesses allowed.")
    print("=" * 40)

    while incorrect_guesses < max_attempts:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Guessed letters:", guessed_letters)
        print("Incorrect guesses:",
              incorrect_guesses, "/", max_attempts)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations,", student_name + "!")
            print("You guessed the word:", secret_word)
            print("YOU WIN!")
            return

        guess = input("Enter one letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

    print("\nGAME OVER!")
    print("The correct word was:", secret_word)
    print("Better luck next time,", student_name + "!")


if __name__ == "__main__":
    hangman()

        