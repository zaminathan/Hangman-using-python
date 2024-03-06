'''
 HANG MAN GAME
This game randomly selects a word  from a list ,displays it as underscore which
represents letters and prompts user  until they either guess letters,either guess
the word or ran out of attempts
'''

import word_list from words


# word_list = ['climb']


def get_word():  # which used to return a random word from word_list
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:  # while not = while false
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():  # 1 if user inputs a letter
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)  # all the letters occurs in a word
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # enumerate used to track both element and its position
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)  # covert it back to string
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():  # 2. if user input the  word
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:  # 3. if user input other than words/letters
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\           # double back slash means single slash represents escape charecter 
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():  # Play again input prompting play again
    word = get_word()
    play(word)
    while input("Play Again? (YES/NO) ").upper() == "YES":
        word = get_word()
        play(word)


if __name__ == "__main__":  # code fragment program will run by running our script on the command line.
    main()

